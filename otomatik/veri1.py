import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute("SELECT * FROM teklif_teklif ORDER BY id DESC LIMIT 1")
row = cursor.fetchone()

A = 'ALICI FIRMA TARAFINDAN'
S = 'SATICI FIRMA TARAFINDAN'
toemail = row[1]
firma = row[2]
usmodel = row[3]
indikator = row[4]
yazar = row[19]
insaat = row[5]
vinc = row[6]
nakliye = row[7]
uzunluk = row[8]
tonaj = row[9]
teslimatgun = row[10]
onodeme = row[11]
cekvade = row[12]
teklifsuresi = row[13]
ekmasraf = row[14]
insaatucret = row[15]
vincucret = row[16]
nakliyeucret = row[17]

print(toemail)

conn.close()