# Generated by Django 4.2.3 on 2023-07-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teklif', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teklif',
            name='insaat',
            field=models.CharField(choices=[('ALICI FIRMA TARAFINDAN', 'Alıcı Firma Tarafından'), ('SATICI FIRMA TARAFINDAN', 'Satıcı Firma Tarafından')], max_length=100),
        ),
        migrations.AlterField(
            model_name='teklif',
            name='nakliye',
            field=models.CharField(choices=[('ALICI FIRMA TARAFINDAN', 'Alıcı Firma Tarafından'), ('SATICI FIRMA TARAFINDAN', 'Satıcı Firma Tarafından')], max_length=100),
        ),
        migrations.AlterField(
            model_name='teklif',
            name='vinc',
            field=models.CharField(choices=[('ALICI FIRMA TARAFINDAN', 'Alıcı Firma Tarafından'), ('SATICI FIRMA TARAFINDAN', 'Satıcı Firma Tarafından')], max_length=100),
        ),
    ]
