from django.contrib import admin

# Register your models here.
from .models import Publisher, Author, Book, DjangoUser


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'


class DjangoUserAdmin(admin.ModelAdmin):
    list_display = ('which_auth',)


admin.site.register(DjangoUser, DjangoUserAdmin)
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
