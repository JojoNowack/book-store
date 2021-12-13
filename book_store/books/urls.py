# book_store -> url
from django.urls import path, include

from books.views import getdetails
from books.views import booksmainpage,cancelproduct


urlpatterns = [


    path('', booksmainpage,name='books-site'),
    path('products/', getdetails, name='products'),
    path('products/cancel/', cancelproduct, name='cancel')
] 
    
