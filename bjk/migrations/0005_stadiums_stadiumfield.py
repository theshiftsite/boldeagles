# Generated by Django 2.0 on 2018-10-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bjk', '0004_auto_20181023_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadiums',
            name='StadiumField',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
