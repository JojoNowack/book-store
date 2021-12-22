from django.contrib import admin
from .models import Book,Category
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title','book_author','isavailable','year','Genre')
    #list_display = ('title','Author','isavailable','year','Genre')
    search_fields = ('title','genre','book_author')
    readonly_fields = ('totalorders','isavailable')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    #def Author(self, obj):
      #  return "\n".join([p.author_name for p in obj.book_author.all()])
    def Genre(self, obj):
        return "\n".join([p.genre for p in obj.genre.all()])

admin.site.register(Book,BooksAdmin)
admin.site.register(Category)