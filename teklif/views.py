from django.shortcuts import render, redirect
from .forms import TeklifForm
# from django.views.decorators.csrf import csrf_protect
import time
# from otomatik.veri import *
# from otomatik.veri1 import *
# from otomatik.topdf import *
# from otomatik.tecnical import *
# from otomatik.myemail import *
# from otomatik.getOffering import *
# if(usmodel=='B'):
#     from otomatik.infoB import *
# elif(usmodel=='C'):
#     from otomatik.infoC import *
# elif(usmodel=='CB'):
#     from otomatik.infoCB import *
# elif(usmodel=='CC'):
#     from otomatik.infoCC import *
# elif(usmodel=='V'):
#     from otomatik.infoV import *
# elif(usmodel=='I'):
#     from otomatik.infoI import *


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
    


