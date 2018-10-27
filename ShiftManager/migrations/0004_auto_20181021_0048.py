# Generated by Django 2.1.2 on 2018-10-20 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShiftManager', '0003_auto_20181021_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('LeaveTypeCode', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='İzin Kodu')),
                ('LeaveTypeDescription', models.CharField(max_length=100, verbose_name='İzin Açıklaması')),
                ('CreatedDate', models.DateField(verbose_name='Oluşturulduğu Tarih')),
                ('IsBlocked', models.BooleanField(default=1, verbose_name='Kullanım Dışı')),
                ('CreatedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftTypes',
            fields=[
                ('ShiftCode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ShiftName', models.CharField(max_length=100)),
                ('CreatedDate', models.DateField(verbose_name='Oluşturulduğu Tarih')),
                ('IsBlocked', models.BooleanField(default=1, verbose_name='Kullanım Dışı')),
                ('CreatedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı')),
            ],
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='CreatedUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan Kullanıcı'),
        ),
    ]