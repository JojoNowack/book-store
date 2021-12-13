from django.contrib import admin
from .models import Book, Category
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'book_author', 'quantity')

admin.site.register(Book,BookAdmin)
admin.site.register(Category)


