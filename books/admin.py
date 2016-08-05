from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Register your models here.
from .models import Authenticationbackend, Organization, Projects


class AuthenticationbackendAdminInline(admin.StackedInline):
    model = Authenticationbackend


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (AuthenticationbackendAdminInline, )


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Identifier')


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'PrId', 'StartDate', 'Status', 'ProjectHead')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Projects, ProjectsAdmin)

