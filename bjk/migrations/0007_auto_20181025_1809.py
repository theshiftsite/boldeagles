# Generated by Django 2.0 on 2018-10-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bjk', '0006_auto_20181025_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individuals',
            name='IndividualCategory',
            field=models.CharField(choices=[('1', 'GRUP-1'), ('2', 'GRUP-2')], max_length=50, verbose_name='Kişi Grubu'),
        ),
        migrations.AlterField(
            model_name='individuals',
            name='IndividualGroup',
            field=models.CharField(choices=[('1', 'GRUP-1'), ('2', 'GRUP-2')], max_length=50, verbose_name='Kişi Grubu'),
        ),
    ]
