

def run(instance = None):
    from teklif.models import Teklif
    if instance:
        print(dir(instance))
        data = instance
        print(f'data1 {data.id}')
        # return data
    else:
        # Son eklenen teklifi almak için ID'ye göre sıralayıp ilk nesneyi alın
        son_teklif = Teklif.objects.all().order_by('-id').first()
        data = son_teklif
        print(f'data2 {data}')
        # return data
    
    from django.conf import settings
    from .tecnical import towordtecnical
    from .myemail import sendemail
    from .topdf import wordtopdf
    import os 
    from .getOffering import toword
    from .veri1 import getdata, delete_docx_file
    veri1_dizini = os.path.join(settings.BASE_DIR, 'otomatik/')
    
    firma, usmodel, indikator, insaat, vinc, nakliye, uzunluk, tonaj, teslimatgun, onodeme, cekvade, teklifsuresi, dosya1, dosya2, sender_email, sender_password, recipient_email, subject, message1,pdf_dizini, word_dizini = getdata(data.id)

    #******************WORD*********************************
    toword(firma,insaat, vinc, nakliye, uzunluk, tonaj ,teslimatgun, onodeme, cekvade, teklifsuresi)
    # ***************TO-PDF***********************************
    wordtopdf(f'{word_dizini}/{dosya1}.docx',f'{pdf_dizini}/{dosya1}.pdf')
    # ******************WORD*********************************
    towordtecnical(usmodel, indikator,uzunluk)
    # ***************TO-PDF***********************************
    wordtopdf(f'{word_dizini}/{dosya2}.docx',f'{pdf_dizini}/{dosya2}.pdf')
    # ******************Preview*********************************
    sendemail(sender_email, sender_password, recipient_email, subject, message1)
    # ******************delete*********************************
    delete_docx_file(os.path.join(settings.BASE_DIR, f'otomatik/word/{dosya1}.docx'))
    delete_docx_file(os.path.join(settings.BASE_DIR, f'otomatik/word/{dosya2}.docx'))
    delete_docx_file(os.path.join(settings.BASE_DIR, f'{dosya1}.pdf'))
    delete_docx_file(os.path.join(settings.BASE_DIR, f'{dosya2}.pdf'))
