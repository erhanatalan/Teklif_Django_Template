from veri import *
from get_info_from_goolesheets import *


if(usmodel == 'V'):
    ara='IPE ÇELİK'
    rampaharic = (7/16)*uzunluk
    mekanikgaranti = 5
    dahil =f''
    rmp = f''
    if(tonaj == 60):
        fiyat = getinfo(sheet, f'{usmodel}{uzunluk}') + ekstrafiyat
    elif(tonaj == 80):
        fiyat = getinfo(sheet, f'{usmodel}{uzunluk+1}') + ekstrafiyat

        
    if(uzunluk==6 or uzunluk==8):
        platform = 2
    elif(uzunluk==12):
        platform = 3
    elif(uzunluk==14 or uzunluk==16 or uzunluk==18):
        platform = 4
    elif(uzunluk==20):
        platform = 5
    mekanik = f'Çelik Konstrüksiyon'

loadcell = (platform * 2) + 2