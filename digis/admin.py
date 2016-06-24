from django.contrib import admin

# Register your models here.
from .models import Members, AdminstrativeMetaData


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


class AdminstrativeMetaDataAdmin(admin.ModelAdmin):
    list_display = ('SubmittingOrganization', 'OrganizationIdentifier', 'ContractNumber')

admin.site.register(Members, MemberAdmin)
admin.site.register(AdminstrativeMetaData, AdminstrativeMetaDataAdmin)
