from veri import *
from get_info_from_goolesheets import *

# *************************
if(tonaj==60 or tonaj==80):
    kalinlik1='270'
    kalinlik2='200'
    kalinlik3='140'
    sackalinligi=8
    fiyat = getinfo(sheet, f'{usmodel}{uzunluk}') + ekstrafiyat
elif(tonaj==100 or tonaj==120):
    kalinlik1='300'
    kalinlik2='240'
    kalinlik3='160'
    sackalinligi=10
    fiyat = getinfo(sheet, f'{usmodel}{uzunluk+1}') + ekstrafiyat
# *************************
if(uzunluk==6):
    platform = 1
    ipeadet1= 6
    yankorkuluk=platform*2
    uzunluk1=6000
    adet2=platform
    uzunluk2=uzunluk1
elif(uzunluk==8):
    platform = 2
    ipeadet1= 12
    yankorkuluk=platform*2
    uzunluk1=4000
    adet2=platform
    uzunluk2=uzunluk1
    # uzunluk3=
elif(uzunluk==10):
    platform = 3
    ipeadet1= f'12\n6'
    yankorkuluk=f'4\n2'
    uzunluk1=f'3000\n4000'
    adet2=f'2\n1'
    uzunluk2=uzunluk1
    # uzunluk3=
elif(uzunluk==12):
    platform = 3
    ipeadet1= 24
    yankorkuluk=platform*2
    uzunluk1 = 4000
    adet2=platform
    uzunluk2=uzunluk1
    # uzunluk3=
elif(uzunluk==14):
    if(tonaj==60 or tonaj==80):
        platform = 3
        ipeadet1= f'12\n6'
        yankorkuluk=f'4\n2'
        uzunluk1 = f'4000\n6000'
        adet2=f'2\n1'
        uzunluk2=uzunluk1
        # uzunluk3=
    elif(tonaj==100 or tonaj==120):
        platform = 4
        ipeadet1= f'12\n12'
        yankorkuluk=f'4\n4'
        uzunluk1 = f'3000\n4000'
        adet2=platform
        uzunluk2=uzunluk1
        # uzunluk3=
elif(uzunluk==16 ):
    if(tonaj==60 or tonaj==80):
        platform = 3
        ipeadet1= f'12\n6'
        yankorkuluk=f'4\n2'
        uzunluk1 = f'6000\n4000'
        adet2=f'2\n1'
        uzunluk2=uzunluk1
        # uzunluk3=
    elif(tonaj==100 or tonaj==120):
        platform = 4
        ipeadet1= f'24'
        yankorkuluk=f'8'
        uzunluk1 = f'4000'
        adet2=platform
        uzunluk2=uzunluk1
        # uzunluk3=
elif(uzunluk==18):
    if(tonaj==60 or tonaj==80):
        platform = 3
        ipeadet1= f'18'
        yankorkuluk=f'6'
        uzunluk1 = f'6000'
        adet2=platform
        uzunluk2=uzunluk1
        # uzunluk3=
    elif(tonaj==100 or tonaj==120):
        platform = 5
        ipeadet1= f'18\n12'
        yankorkuluk=f'10'
        uzunluk1 = f'4000\n3000'
        adet2=f'3\n2'
        uzunluk2=uzunluk1
        # uzunluk3=
elif(uzunluk==20):
    if(tonaj==60 or tonaj==80):
        platform = 4
        ipeadet1= f'24'
        yankorkuluk=f'8'
        uzunluk1 = f'5000'
        adet2=platform
        uzunluk2=uzunluk1
        # uzunluk3=
    elif(tonaj==100 or tonaj==120):
        platform = 5
        ipeadet1= f'12\n18'
        yankorkuluk=f'10'
        uzunluk1 = f'4000\n3000'
        adet2=f'2\n3'
        uzunluk2=uzunluk1
        # uzunluk3=
elif(uzunluk==22):
    if(tonaj==60 or tonaj==80):
        platform = 4
        ipeadet1= f'12\n12'
        yankorkuluk=f'8'
        uzunluk1 = f'6000\n5000'
        adet2=f'2\n2'
        uzunluk2=uzunluk1
        # uzunluk3=
    elif(tonaj==100 or tonaj==120):
        platform = 6
        ipeadet1= f'24\n12'
        yankorkuluk=f'12'
        uzunluk1 = f'4000\n3000'
        adet2=f'4\n2'
        uzunluk2=uzunluk1
        # uzunluk3=
# ************************* 
mekanik = f'Çelik Konstrüksiyon'
ara='IPE ÇELİK'
rampaharic = (9/16)*uzunluk
mekanikgaranti = 5
dahil =f''
rmp = f''
genislik=3
loadcell = (platform * 2) + 2
uzunluk3=f'800\n200'
adet3=f'{uzunluk}\n{uzunluk*4}'
adet4=f'{genislik*uzunluk}'
civata= (platform-1)*2*2




