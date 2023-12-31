# Generated by Django 4.2.3 on 2023-07-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teklif', '0003_alter_teklif_cekvade_alter_teklif_indikator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teklif',
            name='insaat',
            field=models.CharField(choices=[('ALICI FIRMA TARAFINDAN', 'Alıcı Firma Tarafından'), ('SATICI FIRMA TARAFINDAN', 'Satıcı Firma Tarafından')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='teklif',
            name='nakliye',
            field=models.CharField(choices=[('ALICI FIRMA TARAFINDAN', 'Alıcı Firma Tarafından'), ('SATICI FIRMA TARAFINDAN', 'Satıcı Firma Tarafından')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='teklif',
            name='vinc',
            field=models.CharField(choices=[('ALICI FIRMA TARAFINDAN', 'Alıcı Firma Tarafından'), ('SATICI FIRMA TARAFINDAN', 'Satıcı Firma Tarafından')], default=1, max_length=100),
        ),
    ]
