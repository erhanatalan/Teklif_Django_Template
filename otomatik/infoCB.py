from veri import *
from get_info_from_goolesheets import *

if(usmodel == 'CB'):
    
    if(tonaj==60):
        kalinlik1='200'
        fiyat = getinfo(sheet, f'E{uzunluk}') + ekstrafiyat
    elif(tonaj==80):
        kalinlik1='240'
        fiyat = getinfo(sheet, f'E{uzunluk+1}') + ekstrafiyat
    elif(tonaj==100):
        kalinlik1='300'
    rmp = f''
    if(uzunluk==6 or uzunluk==8):
        platform = 2
    elif(uzunluk==10 or uzunluk==12):
        platform = 3
    elif(uzunluk==14 or uzunluk==16 or uzunluk==18):
        platform = 4
    elif(uzunluk==20):
        platform = 5
    elif(uzunluk==22):
        platform = 6
    
mekanik = f'Yarı Çelik Yarı Beton Konstrüksiyon'
ara='U ÇELİK'
rampaharic = (28/16)*uzunluk
mekanikgaranti = 10
rampadahil = rampaharic + 7
dahil =f''
loadcell = (platform * 2) + 2