from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display=('borrow_date','return_date','book_borrowed', 'users')
# Register your models here.
admin.site.register(Order, OrderAdmin)