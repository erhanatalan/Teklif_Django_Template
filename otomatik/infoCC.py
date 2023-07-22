from veri import *
from get_info_from_goolesheets import *


if(usmodel == 'CC'):
    
    if(tonaj==60 or tonaj==80):
        kalinlik1='270'
        fiyat = getinfo(sheet, f'G{uzunluk}') + ekstrafiyat
    elif(tonaj==100 or tonaj==120):
        kalinlik1='300'
        fiyat = getinfo(sheet, f'G{uzunluk+1}') + ekstrafiyat
    rmp = f''
    if(uzunluk==6):
        platform = 1
    elif(uzunluk==8 or uzunluk==10 or uzunluk==12):
        platform = 3
    elif(uzunluk==14 or uzunluk==16 ):
        if(tonaj==60 or tonaj==80):
            platform = 3
        elif(tonaj==100 or tonaj==120):
            platform = 4
    elif(uzunluk==18):
        if(tonaj==60 or tonaj==80):
            platform = 3
        elif(tonaj==100 or tonaj==120):
            platform = 5
    elif(uzunluk==20):
        if(tonaj==60 or tonaj==80):
            platform = 4
        elif(tonaj==100 or tonaj==120):
            platform = 5
    elif(uzunluk==22):
        if(tonaj==60 or tonaj==80):
            platform = 4
        elif(tonaj==100 or tonaj==120):
            platform = 6

            
mekanik = f'Çelik Konstrüksiyon'
ara='U ÇELİK'
rampaharic = (9/16)*uzunluk
mekanikgaranti = 5
dahil =f''
loadcell = (platform * 2) + 2