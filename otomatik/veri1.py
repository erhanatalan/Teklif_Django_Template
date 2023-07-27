import sqlite3
import os
from django.conf import settings
from django.db import connections
from teklif.models import Teklif
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

# conn = sqlite3.connect('db.sqlite3')
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM teklif_teklif ORDER BY id DESC LIMIT 1")
# row = cursor.fetchone()

# A = 'ALICI FIRMA TARAFINDAN'
# S = 'SATICI FIRMA TARAFINDAN'
# toemail = row[1]
# firma = row[2]
# usmodel = row[3]
# indikator = row[4]
# yazar = row[19]
# insaat = row[5]
# vinc = row[6]
# nakliye = row[7]
# uzunluk = row[8]
# tonaj = row[9]
# teslimatgun = row[10]
# onodeme = row[11]
# cekvade = row[12]
# teklifsuresi = row[13]
# ekmasraf = row[14]
# insaatucret = row[15]
# vincucret = row[16]
# nakliyeucret = row[17]
latest_teklif = Teklif.objects.latest('id')
toemail = latest_teklif.toemail
firma = latest_teklif.firma
usmodel = latest_teklif.usmodel
indikator = latest_teklif.indikator
yazar = latest_teklif.yazar
insaat = latest_teklif.insaat
vinc = latest_teklif.vinc
nakliye = latest_teklif.nakliye
uzunluk = latest_teklif.uzunluk
tonaj = latest_teklif.tonaj
teslimatgun = latest_teklif.teslimatgun
onodeme = latest_teklif.onodeme
cekvade = latest_teklif.cekvade
teklifsuresi = latest_teklif.teklifsuresi
ekmansraf = latest_teklif.ekmansraf
insaatucret = latest_teklif.insaatucret
vincucret = latest_teklif.vincucret
nakliyeucret = latest_teklif.nakliyeucret
# print(row)

# cursor.execute("SELECT * FROM teklif_teklif ORDER BY id ASC LIMIT 1")
# row1 = cursor.fetchone()

# print(row1)

# conn.close()