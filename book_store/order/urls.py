# book_store -> url
from django.urls import path, include

from order.views import qrcode,admin_borrow

urlpatterns = [
    path('', qrcode,name='order-site'),
    path('borrow/', admin_borrow)

] 
    
