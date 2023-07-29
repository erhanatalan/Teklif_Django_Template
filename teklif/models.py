from django.db import models

# Create your models here.
class Teklif(models.Model):
    A = 'Alıcı Firma Tarafından'
    S = 'Satıcı Firma Tarafından'
    B = 'B'
    C = 'C'
    CB = 'CB'
    CC = 'CC'
    V = 'V'
    I = 'I'
    X='ABS-B3'
    K='ABS-I1'
    Q= 'Erhan ATALAN'
    W= 'Serdar BULUT'
    E= 'Davut ATALAN'

    KIM_CHOICES = [
        (A, 'Alıcı Firma Tarafından'),
        (S, 'Satıcı Firma Tarafından'),
    ]
    TONAJ_CHOICES = [
        (30, 30),
        (60, 60),
        (80, 80),
        (100, 100),
        (120, 120),
    ]
    UZUNLUK_CHOICES = [
        (6, 6),
        (8, 8),
        (10, 10),
        (12, 12),
        (14, 14),
        (16, 16),
        (18, 18),
        (20, 20),
        (22, 22),
    ]
    USMODEL_CHOICES = [
        (B, 'B'),
        (C, 'C'),
        (CB, 'CB'),
        (CC, 'CC'),
        (V, 'V'),
        (I, 'I'),
    ]
    INDIKATOR_CHOICES = [
        (X, 'ABS-B3'),
        (K, 'ABS-I1'),
    ]
    YAZAR_CHOICES = [
        (Q, 'Erhan ATALAN'),
        (W, 'Serdar BULUT'),
        (E, 'Davut ATALAN'),
    ]
    CEKVADE_CHOICES = [
        (30, 30),
        (60, 60),
        (90, 90),
    ]
    
    toemail = models.EmailField()
    firma = models.CharField(max_length=100)
    usmodel = models.CharField(max_length=5, choices=USMODEL_CHOICES)
    indikator = models.CharField(max_length=10, choices=INDIKATOR_CHOICES)
    yazar = models.CharField(max_length=100, choices=YAZAR_CHOICES)
    # tel = models.CharField(max_length=20, default='+90 535 610 04 77')
    insaat = models.CharField(max_length=100, choices=KIM_CHOICES)
    vinc = models.CharField(max_length=100, choices=KIM_CHOICES)
    nakliye = models.CharField(max_length=100, choices=KIM_CHOICES)
    uzunluk = models.IntegerField(default=16, choices=UZUNLUK_CHOICES)
    tonaj = models.IntegerField(default=80, choices=TONAJ_CHOICES)
    teslimatgun = models.IntegerField(default=15)
    onodeme = models.IntegerField(default=40)
    cekvade = models.IntegerField(default=60, choices=CEKVADE_CHOICES)
    teklifsuresi = models.IntegerField(default=5)
    ekmasraf = models.IntegerField(default=0)
    insaatucret = models.IntegerField(default=0)
    vincucret = models.IntegerField(default=0)
    nakliyeucret = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
