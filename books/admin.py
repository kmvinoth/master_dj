from django.contrib import admin
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from eav.models import Value

# Register your models here.
from .models import Organization, Projects, Deposit, DataObject


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Identifier')


class PrAdmin(admin.ModelAdmin):
    list_display = ('Name', 'organization')


class DepositAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')


class DataObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'deposit')


admin.site.register(Deposit, DepositAdmin)
admin.site.register(DataObject, DataObjectAdmin)
admin.site.register(Projects, PrAdmin)
admin.site.register(Organization, OrganizationAdmin)

