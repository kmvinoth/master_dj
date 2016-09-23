from django.contrib import admin

# Register your models here.
from .models import Projects, Deposit, DataObject, KeyLabelType, MetadataSet, Value, ProjectAdmin, Roles


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name',)


class Projectadminad(admin.ModelAdmin):
    list_display = ('user', 'project', 'role')


class Roleadmin(admin.ModelAdmin):
    list_display = ('role',)


class DepositAdmin(admin.ModelAdmin):
    list_display = ('project',)


class DataObjectAdmin(admin.ModelAdmin):
    list_display = ('deposit',)


class KeyLabelTypeAdmin(admin.ModelAdmin):
    list_display = ('key', 'label', 'datatype')


class PrMdSetAdmin(admin.ModelAdmin):
    list_display = ('project', 'klt')


class ValueAdmin(admin.ModelAdmin):
    list_display = ('metadataset', 'value_text', 'value_int', 'value_float')


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Roles, Roleadmin)
admin.site.register(MetadataSet, PrMdSetAdmin)
admin.site.register(ProjectAdmin, Projectadminad)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(DataObject, DataObjectAdmin)
admin.site.register(KeyLabelType, KeyLabelTypeAdmin)
admin.site.register(Value, ValueAdmin)
