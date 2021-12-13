from django.contrib import admin
from .models import Book
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title','book_author','isavailable','year','genre')
    search_fields = ('title','genre','book_author')
    readonly_fields = ('totalorders','isavailable')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Book,BooksAdmin)