from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from river.models.fields.state import StateField


# Create your models here.
class ShiftTypes(models.Model):
    ShiftCode = models.CharField(max_length=10, primary_key=True)
    ShiftName = models.CharField(max_length=100)
    CreatedDate = models.DateField(verbose_name='Oluşturulduğu Tarih')
    CreatedUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Oluşturan Kullanıcı')
    IsBlocked = models.BooleanField(default=1, verbose_name='Kullanım Dışı')
    Approve = StateField()

    class Meta:
        verbose_name_plural = 'Shift Tipi'
        verbose_name = 'Shift Tipi'

    def publish(self):
        self.CreatedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.ShiftName


class LeaveType(models.Model):
    LeaveTypeCode = models.CharField(max_length=10, primary_key=True, verbose_name='İzin Kodu')
    LeaveTypeDescription = models.CharField(max_length=100, verbose_name='İzin Açıklaması')
    CreatedDate = models.DateField(verbose_name='Oluşturulduğu Tarih')
    CreatedUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Oluşturan Kullanıcı')
    IsBlocked = models.BooleanField(default=1, verbose_name='Kullanım Dışı')

    def publish(self):
        self.CreatedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.LeaveTypeDescription


class JobTitle(models.Model):
    JobTitleCode = models.CharField(max_length=10, primary_key=True, verbose_name='Ünvan Kodu')
    JobTitleDescription = models.CharField(max_length=100, blank=True, null=False, verbose_name='Ünvan Açıklaması')
    IsBlocked = models.BooleanField(default=1, verbose_name='Kullanım Dışı')
    CreatedDate = models.DateField
    CreatedUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Oluşturan Kullanıcı')

    class Meta:
        verbose_name = 'Ünvan'
        verbose_name_plural = 'Ünvanlar'

    def publish(self):
        self.CreatedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.JobTitleDescription


class LeaveApplication(models.Model):
    EmployeeCode = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Personel Kodu')
    LeaveType = models.ForeignKey(LeaveType, on_delete=models.CASCADE, verbose_name='İzin Tipi')
    LeaveStartDate = models.DateField(verbose_name='Başlangıç Tarihi')
    LeaveEndDate = models.DateField(verbose_name='Bitiş Tarihi')
    LeaveDesc = models.TextField(max_length=100, verbose_name='Açıklama')
    IsBlocked = models.BooleanField(verbose_name='Kullanım Dışı',default=0)
    CreatedDate = models.DateField
    StateStatus = StateField(verbose_name='Status')

    class Meta:
        verbose_name_plural = 'Yıllık İzin'
        verbose_name = 'Yıllık İzin'

    def publish(self):
        self.CreatedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.LeaveDesc
