from django.contrib import admin


# Register your models here.
from .models import Organization, Projects, Klt, PrMdSet, Deposit, DataObject, DepositMdSet, DataObjectMdSet


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Identifier')


class KltAdmin(admin.ModelAdmin):
    list_display = ('key','label')


class PrAdmin(admin.ModelAdmin):
    list_display = ('Name', 'ProjectHead','organization')


class PrMdsetAdmin(admin.ModelAdmin):
    list_display = ('project', 'klt')


class DepositAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')


class DepositMdsetAdmin(admin.ModelAdmin):
    list_display = ('project','deposit', 'klt')


class DataObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'deposit')


class DataobjectMdsetAdmin(admin.ModelAdmin):
    list_display = ('dataobject', 'klt')


admin.site.register(PrMdSet, PrMdsetAdmin)
admin.site.register(DepositMdSet, DepositMdsetAdmin)
admin.site.register(DataObjectMdSet, DataobjectMdsetAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(DataObject, DataObjectAdmin)
admin.site.register(Projects, PrAdmin)
admin.site.register(Klt, KltAdmin)
admin.site.register(Organization, OrganizationAdmin)

