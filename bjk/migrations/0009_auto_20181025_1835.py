# Generated by Django 2.0 on 2018-10-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bjk', '0008_auto_20181025_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcreditationForIndividuals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AcreditationForFixedCardNumber', models.CharField(blank=True, max_length=20, verbose_name='Sabit Kart NO')),
                ('AcreditationForIdentityNum', models.CharField(blank=True, max_length=20, verbose_name='TC Kimlik NO')),
                ('AcreditationForIsOutlander', models.BooleanField(default=0, verbose_name='Yabancı mı?')),
                ('AcreditationForIndividualGroup', models.CharField(choices=[('1', 'GRUP-1'), ('2', 'GRUP-2')], max_length=50, verbose_name='Kişi Grubu')),
                ('AcreditationForIndividualCategory', models.CharField(choices=[('1', 'GRUP-1'), ('2', 'GRUP-2')], max_length=50, verbose_name='Kişi Grubu')),
                ('AcreditationForLicenceNumber', models.BigIntegerField(verbose_name='Lisan Numarası')),
                ('AcreditationForIndividualFirstName', models.CharField(max_length=30, verbose_name='Adı')),
                ('AcreditationForIndividualLastName', models.CharField(max_length=30, verbose_name='SoyAdı')),
                ('AcreditationForIndividualCompany', models.CharField(max_length=30, verbose_name='Adı')),
                ('AcreditationForIndividualJobTitle', models.CharField(max_length=30, verbose_name='Görev')),
                ('AcreditationForIndividualShirtNumber', models.BigIntegerField(verbose_name='Yelek No')),
                ('AcreditationForIndividualPhoneNumber', models.CharField(max_length=10, verbose_name='Telefon No')),
                ('AcreditationForIndividualEmailAddress', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Akreditasyon',
                'verbose_name_plural': 'Akreditasyon',
            },
        ),
        migrations.AddField(
            model_name='individuals',
            name='AcreditationForAKR',
            field=models.BooleanField(default=False, verbose_name='Akr'),
        ),
        migrations.AddField(
            model_name='individuals',
            name='AcreditationForBAS',
            field=models.BooleanField(default=False, verbose_name='Bas'),
        ),
        migrations.AddField(
            model_name='individuals',
            name='AcreditationForCG',
            field=models.BooleanField(default=False, verbose_name='CG'),
        ),
        migrations.AddField(
            model_name='individuals',
            name='AcreditationForESG',
            field=models.BooleanField(default=False, verbose_name='Eşg'),
        ),
        migrations.AddField(
            model_name='individuals',
            name='AcreditationForSIL',
            field=models.BooleanField(default=False, verbose_name='Sil'),
        ),
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
