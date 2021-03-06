# Generated by Django 2.1.2 on 2018-10-20 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtitle',
            name='IsBlocked',
            field=models.BooleanField(default=1, verbose_name='Kullanım Dışı'),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='JobTitleCode',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Ünvan Kodu'),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='JobTitleDescription',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ünvan Açıklaması'),
        ),
    ]
