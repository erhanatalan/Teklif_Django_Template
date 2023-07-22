from veri import *
from get_info_from_goolesheets import *


    
if(tonaj == 60 or tonaj == 80):
    fiyat = getinfo(sheet, f'{usmodel}{uzunluk}') + ekstrafiyat
elif(tonaj == 100 or tonaj == 120):
    fiyat = getinfo(sheet, f'{usmodel}{uzunluk+1}') + ekstrafiyat
       
if(uzunluk==16):
    platform = 3


mekanik = f'Çelik Konstrüksiyon'
ara='IPE ÇELİK'
rampaharic = (11/16)*uzunluk
mekanikgaranti = 5
dahil =f''
rmp = f''
loadcell = (platform * 2) + 2
    # *******************************************


