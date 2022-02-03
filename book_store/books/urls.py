# book_store -> url
from django.urls import path, include

from books.views import getdetails
from books.views import booksmainpage


urlpatterns = [


    path('', booksmainpage,name='books-site'),
    path('products/', getdetails, name='products')
] 
    
