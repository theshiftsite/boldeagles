from django.db import models
from django.utils import timezone

# CHOICES
Individuals_GROUP = {
    ('1', 'GRUP-1'),
    ('2', 'GRUP-2'),

}

Individuals_CAT = {
    ('1', 'Kategori-1'),
    ('2', 'Kategori-2'),

}


# Create your models here.
class Partners(models.Model):
    PartnerId = models.CharField(max_length=10, primary_key=True, verbose_name='Kurum Kodu')
    PartnerName = models.CharField(max_length=250, verbose_name='Kurum Adı')
    PartnerAddressCountry = models.CharField(max_length=50, verbose_name='Ülke')
    PartnerAddressCity = models.CharField(max_length=50, verbose_name='Şehirr')
    PartnerAddressDistrict = models.CharField(max_length=50, verbose_name='İlçe')
    PartnerAddressAdddresLine = models.CharField(max_length=50, verbose_name='Adres')

    def publish(self):
        self.save()

    def __str__(self):
        return self.PartnerName

    class Meta:
        verbose_name = 'Kurumlar'


class Stadiums(models.Model):
    StadiumCode = models.CharField(max_length=100, primary_key=True, verbose_name='Stadyum Kodu')
    StadiumName = models.CharField(max_length=200, verbose_name='Stadyum Adı')
    StadiumCapacity = models.CharField(max_length=200)
    StadiumCity = models.CharField(max_length=100)
    StadiumField = models.CharField(max_length=100)
    StadiumFieldType = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Stadyum'

    def publish(self):
        self.save()

    def __str__(self):
        return self.StadiumName


class GameTournament(models.Model):
    TournamentId = models.CharField(max_length=100, primary_key=True)
    TournamentCountry = models.CharField(max_length=100)
    TournamentName = models.CharField(max_length=100)
    Organization = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ligler & Turnuvalar'
        verbose_name_plural = 'Ligler & Turnuvalar'

    def publish(self):
        self.save()

    def __str__(self):
        return self.TournamentName


class Game(models.Model):
    GameCode = models.CharField(max_length=50, primary_key=True, blank=True, null=False, verbose_name='Maç Kodu')
    GameTournament = models.ForeignKey(GameTournament, on_delete=models.CASCADE, verbose_name='Lig')
    GameHome = models.CharField(max_length=50, blank=True, null=False, verbose_name='Ev Sahini')
    GameAway = models.CharField(max_length=50, blank=True, null=False, verbose_name='Misafir')
    GamePlannedDate = models.DateField(verbose_name='Planlandığı Tarih', default=timezone.now)
    StadiumPlanned = models.CharField(max_length=50, blank=True, null=False, verbose_name='Planlanan Stadyum')
    GamePlannedTime = models.TimeField(verbose_name='Planlandığı Saat', default=timezone.timedelta)

    class Meta:
        verbose_name = 'Maçlar'
        verbose_name_plural = 'Maçlar'

    def publish(self):
        self.save()

    def __str__(self):
        return self.GameHome


class Individuals(models.Model):
    FixedCardNumber = models.CharField(max_length=20, blank=True, null=False, verbose_name='Sabit Kart NO')
    IdentityNum = models.CharField(max_length=20, blank=True, null=False, verbose_name='TC Kimlik NO')
    IsOutlander = models.BooleanField(default=0, verbose_name='Yabancı mı?')
    IndividualGroup = models.CharField(choices=Individuals_GROUP, max_length=50, verbose_name='Kişi Grubu')
    IndividualCategory = models.CharField(choices=Individuals_CAT, max_length=50, verbose_name='Kategori')
    LicenceNumber = models.BigIntegerField(verbose_name='Lisan Numarası')
    IndividualFirstName = models.CharField(max_length=30, verbose_name='Adı')
    IndividualLastName = models.CharField(max_length=30, verbose_name='SoyAdı')
    IndividualCompany = models.ForeignKey(Partners, on_delete=models.CASCADE, verbose_name='KurumAdı')
    IndividualJobTitle = models.CharField(max_length=30, verbose_name='Görev')
    IndividualShirtNumber = models.BigIntegerField(verbose_name='Yelek No')
    IndividualPhoneNumber = models.CharField(max_length=10, verbose_name='Telefon No')
    IndividualEmailAddress = models.EmailField(verbose_name='Email')
    AcreditationForAKR = models.BooleanField(verbose_name='Akr', default=False)
    AcreditationForBAS = models.BooleanField(verbose_name='Bas', default=False)
    AcreditationForESG = models.BooleanField(verbose_name='Eşg', default=False)
    AcreditationForSIL = models.BooleanField(verbose_name='Sil', default=False)
    AcreditationForCG = models.BooleanField(verbose_name='CG', default=False)

    class Meta:
        verbose_name_plural = 'Kişi Giriş ve Düzeltme'
        verbose_name = 'Kişi Giriş ve Düzeltme'


class AcreditationForIndividuals(models.Model):
    AcreditationForFixedCardNumber = models.CharField(max_length=20, blank=True, null=False,
                                                      verbose_name='Sabit Kart NO')
    AcreditationForIdentityNum = models.CharField(max_length=20, blank=True, null=False, verbose_name='TC Kimlik NO')
    AcreditationForIsOutlander = models.BooleanField(default=0, verbose_name='Yabancı mı?')
    AcreditationForIndividualGroup = models.CharField(choices=Individuals_GROUP, max_length=50,
                                                      verbose_name='Kişi Grubu')
    AcreditationForIndividualCategory = models.CharField(choices=Individuals_CAT, max_length=50,
                                                         verbose_name='Kişi Grubu')
    AcreditationForLicenceNumber = models.BigIntegerField(verbose_name='Lisan Numarası')
    AcreditationForIndividualFirstName = models.CharField(max_length=30, verbose_name='Adı')
    AcreditationForIndividualLastName = models.CharField(max_length=30, verbose_name='SoyAdı')
    AcreditationForIndividualCompany = models.ForeignKey(Partners, on_delete=models.CASCADE, verbose_name='Kurum Adı')
    AcreditationForIndividualJobTitle = models.CharField(max_length=30, verbose_name='Görev')
    AcreditationForIndividualShirtNumber = models.BigIntegerField(verbose_name='Yelek No')
    AcreditationForIndividualPhoneNumber = models.CharField(max_length=10, verbose_name='Telefon No')
    AcreditationForIndividualEmailAddress = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name_plural = 'Akreditasyon'
        verbose_name = 'Akreditasyon'
