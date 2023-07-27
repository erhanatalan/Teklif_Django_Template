from django.shortcuts import render, redirect
from .forms import TeklifForm
import time
import os
from django.conf import settings
from django.db import transaction

pdf_dizini = os.path.join(settings.BASE_DIR, 'otomatik/pdf')

def offer_success_view(request):
    return render(request, 'offer_success.html')

def teklif_submit_view(request):
    if request.method == 'POST':
        form = TeklifForm(request.POST)
        if form.is_valid():
            form = TeklifForm()
            form.save()
            transaction.commit()
            from otomatik.run import run
            run()
            # pdf_preview()
            return redirect('offer_success_view')
    else:
        form = TeklifForm(initial={'uzunluk': 16, 'tonaj': 80, 'indikator':'ABS-B3', 'usmodel':'B', 'yazar':'Erhan ATALAN'})
    return render(request, 'home.html', {'form': form})



# def pdf_preview(request):
#     if request.method == 'POST':
#         path1 = request.POST.get('Teklif_path')
#         path2 = request.POST.get('Teknik_Veriler_path')
#         images = []

#         for path in [path1, path2]:
#             doc = fitz.open(path)
#             page = doc[0]
#             pix = page.get_pixmap()
#             image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
#             images.append(image)

#         return render(request, 'home.html', {'images': images})

#     return render(request, 'home.html')
    
# def pdf_preview(request):
#     # PDF dosya yollarını burada alın ve modala aktarmak için şablona geçin
#     context = {
#         'Teklif_path': f'{settings.BASE_DIR}/Teklif.pdf',
#         'Teknik_Veriler_path': f'{settings.BASE_DIR}/Teknik_Veriler.pdf'
#     }
#     return render(request, 'home.html', context)

