# Generated by Django 4.2.3 on 2023-07-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teklif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toemail', models.EmailField(max_length=254)),
                ('firma', models.CharField(max_length=100)),
                ('usmodel', models.CharField(choices=[(1, 'B'), (2, 'C'), (3, 'CB'), (4, 'CC'), (5, 'V'), (6, 'I')], default=1, max_length=5)),
                ('indikator', models.CharField(choices=[(1, 'ABS-B3'), (2, 'ABS-I1')], default=1, max_length=10)),
                ('yazar', models.CharField(choices=[(1, 'Erhan ATALAN'), (2, 'Serdar BULUT'), (3, 'Davut ATALAN')], default=1, max_length=100)),
                ('insaat', models.CharField(choices=[(1, 'Alıcı Firma Tarafından'), (2, 'Satıcı Firma Tarafından')], max_length=100)),
                ('vinc', models.CharField(choices=[(1, 'Alıcı Firma Tarafından'), (2, 'Satıcı Firma Tarafından')], max_length=100)),
                ('nakliye', models.CharField(choices=[(1, 'Alıcı Firma Tarafından'), (2, 'Satıcı Firma Tarafından')], max_length=100)),
                ('uzunluk', models.IntegerField(choices=[(6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20), (22, 22)], default=16)),
                ('tonaj', models.IntegerField(choices=[(30, 30), (60, 60), (80, 80), (100, 100), (120, 120)], default=80)),
                ('teslimatgun', models.IntegerField(default=15)),
                ('onodeme', models.IntegerField(default=40)),
                ('cekvade', models.IntegerField(choices=[(1, 30), (2, 60), (3, 90)], default=60)),
                ('teklifsuresi', models.IntegerField(default=5)),
                ('ekmasraf', models.IntegerField(default=0)),
                ('insaatucret', models.IntegerField(default=0)),
                ('vincucret', models.IntegerField(default=0)),
                ('nakliyeucret', models.IntegerField(default=0)),
            ],
        ),
    ]
