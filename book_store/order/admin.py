from django.contrib import admin
from .models import Order
from django.contrib.auth.models import User

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('books','book_borrowed','users','first_name','last_name','return_date','borrow_date')
    def first_name(self, obj):
        return obj.users.first_name
    def last_name(self, obj):
        return obj.users.last_name
    search_fields = ('books__title','users__username')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Order,OrderAdmin)

from django.contrib import admin
from .models import Order
