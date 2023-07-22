from .veri import *
from .veri1 import *
from .topdf import *
from .tecnical import towordtecnical
from .myemail import sendemail
from .getOffering import toword
if(usmodel=='B'):
    from .infoB import *
elif(usmodel=='C'):
    from .infoC import *
elif(usmodel=='CB'):
    from .infoCB import *
elif(usmodel=='CC'):
    from .infoCC import *
elif(usmodel=='V'):
    from .infoV import *
elif(usmodel=='I'):
    from .infoI import *

word_dizini = 'C:/Users/yenic/Desktop/Teklif_Django_Template/otomatik/word/'

pdf_dizini = 'C:/Users/yenic/Desktop/Teklif_Django_Template/otomatik/pdf/'

def run():
    # ******************WORD*********************************
    toword()
    # ***************TO-PDF***********************************
    wordtopdf(f'{word_dizini}/{dosya1}.docx',f'{pdf_dizini}/{dosya1}.pdf')
    # ******************WORD*********************************
    towordtecnical()
    # ***************TO-PDF***********************************
    wordtopdf(f'{word_dizini}/{dosya2}.docx',f'{pdf_dizini}/{dosya2}.pdf')
    # ******************Preview*********************************
    sendemail(sender_email, sender_password, recipient_email, subject, message1)
