from .veri1 import *
import os
from dotenv import load_dotenv
from docx.shared import RGBColor
load_dotenv()

A = 'ALICI FİRMA TARAFINDAN'
S = 'SATICI FİRMA TARAFINDAN'
# ******************************************
model = f'ABS-{usmodel}{uzunluk}T{tonaj}'
kdv = 20
adet = 1
ekstrafiyat = ekmasraf + insaatucret + vincucret + nakliyeucret
if (cekvade==30):
    ekcekodeme = 3  #*%
elif (cekvade==60):
    ekcekodeme = 6  #*%
elif (cekvade==90):
    ekcekodeme = 9  #*%
#* Değiştirilecek alan

# ***************mail************************
mymail = "abskantar@outlook.com"
firma1 = 'ABS ELEKTRONİK TARTI SİSTEMLERİ SAN.TİC.LTD.ŞTİ'
gorev = 'Pazarlama Yöneticisi'

if(yazar=='Erhan ATALAN'):
    tel='+90 535 610 04 77'
elif(yazar=='Serdar BULUT'):
    tel='+90 530 872 04 77'
elif(yazar=='Davut ATALAN'):
    tel='+90 532 131 77 57'

# Example usage
sender_email = mymail
recipient_email = toemail
subject = f'{model} Model Kantar Fiyat Teklifi'
message1 = f'''
<html>
<body>
    <p>​Merhaba,</p>
    <p>​Talep etmiş olduğunuz {uzunluk} metre {tonaj} tonluk kantar ile ilgili fiyat teklifi ekte yer almaktadır.</p>
    <p>Saygılarımla</p>
    <p style='margin-top:50px'>{yazar}</p>
    <p>{gorev}</p>
    <p>{tel}</p>
    <p>{firma1}</p>
</body>
</html>'''


kirmizi = RGBColor(255, 0, 0)
mavi = RGBColor(28, 96, 113)

dosya1 = f'Teklif'
dosya2 = f'Teknik_Veriler'

sheet = os.getenv("KEY")
sender_password = os.getenv("SIFRE")

if(tonaj==30):
    taksimat="10 Kg"
    hassasiyet= '5 Kg'
elif(tonaj==60):
    taksimat="20 Kg"
    hassasiyet= '10 Kg'
elif(tonaj==80):
    taksimat="50 Kg"
    hassasiyet= '25 Kg'
elif(tonaj==100):
    taksimat="50 Kg"
    hassasiyet= '25 Kg'