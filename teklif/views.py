from django.shortcuts import render, redirect
from .forms import TeklifForm
# from django.views.decorators.csrf import csrf_protect
import time
import os
from django.conf import settings

def offer_success_view(request):
    return render(request, 'offer_success.html')

def teklif_submit_view(request):
    if request.method == 'POST':
        form = TeklifForm(request.POST)
        if form.is_valid():
            form.save()
            time.sleep(5)
            from otomatik.run import run
            run()
            return redirect('offer_success_view')  # Eğer teklif başarılı bir şekilde kaydedildiyse başka bir sayfaya yönlendirilebilirsiniz.
        
        run()
    else:
        form = TeklifForm(initial={'uzunluk': 16, 'tonaj': 80, 'indikator':'ABS-B3', 'usmodel':'B', 'yazar':'Erhan ATALAN'})
    return render(request, 'home.html', {'form': form})
    
def pdf_preview(request):
    pdf_dizini = os.path.join(settings.BASE_DIR, 'otomatik/pdf')
    # PDF dosya yollarını burada alın ve modala aktarmak için şablona geçin
    context = {
        'Teklif_path': f'{pdf_dizini}/Teklif.pdf',
        'Teknik_Veriler_path': f'{pdf_dizini}/Teknik_Veriler.pdf'
    }
    return render(request, 'home.html', context)

