from django.contrib import admin

# Register your models here.
from .models import Members


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Members, MemberAdmin)
