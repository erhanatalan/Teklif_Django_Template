from .veri import *
from decimal import Decimal
from .get_info_from_goolesheets import getinfo



rampafiyat=getinfo(sheet, f'{usmodel}1')
foto= 'https://photos.app.goo.gl/7UFco1rcr5ZdS1ua6'
# *************************
if(tonaj==60):
    fiyat = getinfo(sheet, f'{usmodel}{uzunluk}') + ekstrafiyat
    kalinlik1=200
    kalinlik2= 160
    uzunluk2= 500
    kalinlik3=100
    uzunluk3= 1250
elif(tonaj==80):
    fiyat = getinfo(sheet, f'{usmodel}{uzunluk+1}') + ekstrafiyat
    kalinlik1=240
    kalinlik2= 200
    uzunluk2= 750
    kalinlik3=120
    uzunluk3= 1125
elif(tonaj==100):
    kalinlik1=300
    kalinlik2= 240
    uzunluk2= 750
    kalinlik3=160
    uzunluk3= 1125
# *************************
if(uzunluk==6):
    platform = 2
    ipeadet1= 8
    yankorkuluk=platform*2
    uzunluk1 = 3000
    proje=f'https://drive.google.com/file/d/1O4IC2EwEYNXRsxGPidBL-JHx3az4C_bx/view?usp=sharing'
    proje2=f'https://drive.google.com/file/d/1_-eGrDP0No0phpAAv-Y94LkmGrkr1i-B/view?usp=sharing'
elif(uzunluk==8):
    platform = 2
    ipeadet1= 8
    yankorkuluk=platform*2
    uzunluk1 = 4000
    proje=f'https://drive.google.com/file/d/1MmCO42z8K1x3vyiozm09E1HivFjVP-2V/view?usp=sharing'
    proje2=f'https://drive.google.com/file/d/1UgJLAk7X7Rcn5GH3ek2IDJp2tM-YVnfl/view?usp=sharing'
elif(uzunluk==10):
    platform = 3
    ipeadet1= f'8\n4'
    yankorkuluk=f'4\n2'
    uzunluk1 = f'3000\n4000'
    proje=f'{gorev} ile iletişime geçiniz.'
    proje2=f'https://drive.google.com/file/d/1rNV_30QcURHcbSgqfUDWu4ZfZAavU1KV/view?usp=sharing'
elif(uzunluk==12):
    platform = 3
    ipeadet1= 12
    yankorkuluk=platform*2
    uzunluk1 = 4000
    proje=f'https://drive.google.com/file/d/1FR21qpz0ASMdZ5-6J_K68Li3gvm2PgYf/view?usp=sharing'
    proje2=f'https://drive.google.com/file/d/1oDsMer9PAOlphBFexSL7vaJr0Bx3R3Nn/view?usp=sharing'
elif(uzunluk==14):
    platform = 4
    ipeadet1= f'8\n8'
    yankorkuluk=f'4\n4'
    uzunluk1 = f'3000\n4000'
    if(tonaj==60):
        proje=f'{gorev} ile iletişime geçiniz.'
        proje2=f'{gorev} ile iletişime geçiniz.'
    if(tonaj==80):
        proje=f'{gorev} ile iletişime geçiniz.'
        proje2=f'{gorev} ile iletişime geçiniz.'
elif(uzunluk==16):
    platform = 4
    ipeadet1= 16
    yankorkuluk=platform*2
    uzunluk1 = 4000
    if(tonaj==60):
        proje=f'https://drive.google.com/file/d/1mdelDMFZZqkhIytyrJs0mGYbPn5E7-m2/view?usp=sharing'
        proje2=f'https://drive.google.com/file/d/1el2eAMfcprVtToEwUxMSUF60ZRvoiHOm/view?usp=sharing'
    if(tonaj==80):
        proje=f'https://drive.google.com/file/d/1JJkG_4gorfy0PdFtu6JnnW9P4wZUqhQk/view?usp=sharing'
        proje2=f'https://drive.google.com/file/d/1el2eAMfcprVtToEwUxMSUF60ZRvoiHOm/view?usp=sharing'
elif(uzunluk==18):
    platform = 4
    ipeadet1= 16
    yankorkuluk=platform*2
    uzunluk1 = 4500
    if(tonaj==60):
        proje=f'{gorev} ile iletişime geçiniz.'
        proje2=f'{gorev} ile iletişime geçiniz.'
    if(tonaj==80):
        proje=f'{gorev} ile iletişime geçiniz.'
        proje2=f'{gorev} ile iletişime geçiniz.'
elif(uzunluk==20):
    platform = 5
    ipeadet1= 20
    yankorkuluk=platform*2
    uzunluk1 = 4000
    if(tonaj==60):
        proje=f'{gorev} ile iletişime geçiniz.'
        proje2=f'{gorev} ile iletişime geçiniz.'
    if(tonaj==80):
        proje=f'{gorev} ile iletişime geçiniz.'
        proje2=f'{gorev} ile iletişime geçiniz.'
elif(uzunluk==22):
    platform = 6
    ipeadet1= f'16\n8'
    yankorkuluk=f'8\n4'
    uzunluk1 = f'4000\n3000'
    if(tonaj==60):
        proje=f'{gorev} ile iletişime geçiniz.'
        proje2=f'{gorev} ile iletişime geçiniz.'
    if(tonaj==80):
        proje=f'{gorev} ile iletişime geçiniz.'
        proje2=f'{gorev} ile iletişime geçiniz.'
# *************************
ara='U ÇELİK'
rampaharic = (20/16)*uzunluk
mekanikgaranti = 10
rampadahil = rampaharic + 7
dahil =f',rampalar da olursa toplam ağırlık {rampadahil} Ton'
rmp = f'\n4 Adet Hazır Rampa Fiyatı {rampafiyat}₺'
mekanik = 'Yarı Çelik Yarı Beton Konstrüksiyon'
adet2= platform*2
adet3 = uzunluk*2
sackalinligi=3
beton=((3000-100-uzunluk2)/1000)*(kalinlik2/1000)*(uzunluk)
civata= (platform-1)*2*2
rounded_number=Decimal(((3000-100-uzunluk2)/1000)*uzunluk*2)
hasir = round(rounded_number, 2)
loadcell = (platform * 2) + 2
adet4=f'{(uzunluk2/1000)*uzunluk}'