# book_store -> url
from django.urls import path, include

from order.views import qrcode,admin_borrow,admin_borrow_view,finish_orders

urlpatterns = [
    path('', qrcode,name='order-site'),
    path('borrow/', admin_borrow),
    path('borrow/admin',admin_borrow_view,name='admin_order-site'),
    path('borrow/admin/finish',finish_orders)

] 
    
