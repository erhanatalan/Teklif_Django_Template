
def run():
    from teklif.views import s1
    import os
    from django.conf import settings
    from .tecnical import towordtecnical
    from .myemail import sendemail
    from .topdf import wordtopdf
    from .getOffering import toword
    from .veri1 import firma, usmodel, indikator, insaat, vinc, nakliye, uzunluk, tonaj, teslimatgun, onodeme, cekvade, teklifsuresi, dosya1, dosya2, sender_email, sender_password, recipient_email, subject, message1,pdf_dizini, word_dizini,delete_docx_file

    # print(s1[0])
    # ******************WORD*********************************
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