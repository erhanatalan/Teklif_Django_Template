from .veri import *
from .veri1 import *
from .topdf import *
from .tecnical import towordtecnical
from .myemail import sendemail
import os
from django.conf import settings
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


word_dizini = os.path.join(settings.BASE_DIR, 'otomatik/word')

pdf_dizini = os.path.join(settings.BASE_DIR, 'otomatik/pdf')

def delete_docx_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

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

    delete_docx_file(os.path.join(settings.BASE_DIR, f'otomatik/word/{dosya1}.docx'))
    print('1')
    delete_docx_file(os.path.join(settings.BASE_DIR, f'otomatik/word/{dosya2}.docx'))
    print('2')
    delete_docx_file(os.path.join(settings.BASE_DIR, f'{dosya1}.pdf'))
    print('3')
    delete_docx_file(os.path.join(settings.BASE_DIR, f'{dosya2}.pdf'))
    print('4')