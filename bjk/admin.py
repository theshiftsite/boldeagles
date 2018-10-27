
from django.contrib import admin

from .models import Stadiums, GameTournament, Game, Individuals, AcreditationForIndividuals, Partners


# Register your models here.
@admin.register(Partners)
class AdminPartners(admin.ModelAdmin):
    list_display = ('PartnerId', 'PartnerName', 'PartnerAddressCountry','PartnerAddressCity')
    list_filter = ('PartnerId', 'PartnerName', 'PartnerAddressCountry','PartnerAddressCity')

# base Regoin Start
@admin.register(GameTournament)
class AdminGameTournament(admin.ModelAdmin):
    list_display = ('TournamentId', 'TournamentCountry', 'TournamentName', 'Organization')
    list_filter = ('TournamentId', 'TournamentCountry', 'TournamentName', 'Organization')


# base Region End


# TransactionModels
@admin.register(Individuals)
class AdminIndividual(admin.ModelAdmin):
    list_display = ('FixedCardNumber', 'IdentityNum', 'IsOutlander',
                    'IndividualGroup', 'IndividualCategory', 'LicenceNumber',
                    'IndividualFirstName', 'IndividualLastName', 'IndividualCompany',
                    'IndividualJobTitle', 'IndividualShirtNumber',
                    'IndividualPhoneNumber', 'IndividualEmailAddress',)

    list_filter = ('FixedCardNumber', 'IdentityNum', 'IsOutlander',
                   'IndividualGroup', 'IndividualCategory', 'LicenceNumber',
                   'IndividualFirstName', 'IndividualLastName', 'IndividualCompany',
                   'IndividualJobTitle', 'IndividualShirtNumber',
                   'IndividualPhoneNumber', 'IndividualEmailAddress',)
    list_editable = ('IsOutlander',
                     'IndividualGroup', 'IndividualCategory', 'LicenceNumber',
                     'IndividualShirtNumber',
                     'IndividualPhoneNumber', 'IndividualEmailAddress',)


@admin.register(AcreditationForIndividuals)
class AdminAcreditation(admin.ModelAdmin):
    list_display = ('AcreditationForFixedCardNumber', 'AcreditationForIdentityNum', 'AcreditationForIsOutlander',
                    'AcreditationForIndividualGroup', 'AcreditationForIndividualCategory',
                    'AcreditationForLicenceNumber',
                    'AcreditationForIndividualFirstName', 'AcreditationForIndividualLastName',
                    'AcreditationForIndividualCompany',
                    'AcreditationForIndividualJobTitle', 'AcreditationForIndividualShirtNumber',
                    'AcreditationForIndividualPhoneNumber', 'AcreditationForIndividualEmailAddress',)

    list_filter = ( 'AcreditationForFixedCardNumber', 'AcreditationForIdentityNum', 'AcreditationForIsOutlander',
                    'AcreditationForIndividualGroup', 'AcreditationForIndividualCategory',
                    'AcreditationForLicenceNumber',
                    'AcreditationForIndividualFirstName', 'AcreditationForIndividualLastName',
                    'AcreditationForIndividualCompany',
                    'AcreditationForIndividualJobTitle', 'AcreditationForIndividualShirtNumber',
                    'AcreditationForIndividualPhoneNumber', 'AcreditationForIndividualEmailAddress',)

# TransactionModels
