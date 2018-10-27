from django.contrib import admin
from .models import JobTitle, LeaveType, ShiftTypes
from django.urls import reverse


# Register your models here.


@admin.register(JobTitle)
class AdminJobTitle(admin.ModelAdmin):
    list_display = ('JobTitleCode', 'JobTitleDescription', 'CreatedUser', 'IsBlocked')
    list_filter = ('JobTitleCode', 'JobTitleDescription', 'IsBlocked', 'CreatedUser')
    search_fields = ('JobTitleCode', 'JobTitleDescription', 'IsBlocked')


@admin.register(LeaveType)
class AdminLeaveType(admin.ModelAdmin):
    list_display = ('LeaveTypeCode', 'LeaveTypeDescription', 'IsBlocked')
    list_filter = ('LeaveTypeCode', 'LeaveTypeDescription', 'IsBlocked')


@admin.register(ShiftTypes)
class AdminShiftType(admin.ModelAdmin):
    list_display = ('ShiftCode', 'ShiftName', 'Approve')
    list_filter = ('ShiftCode', 'ShiftName')

