# Generated by Django 2.0 on 2018-10-25 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bjk', '0009_auto_20181025_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acreditationforindividuals',
            name='AcreditationForIndividualCategory',
            field=models.CharField(choices=[('2', 'GRUP-2'), ('1', 'GRUP-1')], max_length=50, verbose_name='Kişi Grubu'),
        ),
        migrations.AlterField(
            model_name='acreditationforindividuals',
            name='AcreditationForIndividualCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bjk.Partners', verbose_name='Kurum Adı'),
        ),
        migrations.AlterField(
            model_name='acreditationforindividuals',
            name='AcreditationForIndividualGroup',
            field=models.CharField(choices=[('2', 'GRUP-2'), ('1', 'GRUP-1')], max_length=50, verbose_name='Kişi Grubu'),
        ),
        migrations.AlterField(
            model_name='individuals',
            name='IndividualCategory',
            field=models.CharField(choices=[('2', 'GRUP-2'), ('1', 'GRUP-1')], max_length=50, verbose_name='Kişi Grubu'),
        ),
        migrations.AlterField(
            model_name='individuals',
            name='IndividualCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bjk.Partners', verbose_name='KurumAdı'),
        ),
        migrations.AlterField(
            model_name='individuals',
            name='IndividualGroup',
            field=models.CharField(choices=[('2', 'GRUP-2'), ('1', 'GRUP-1')], max_length=50, verbose_name='Kişi Grubu'),
        ),
    ]