# book_store -> url

from django.contrib import admin
from django.shortcuts import redirect
from . import views
from book_store.views import customhandler404,customhandler500
from django.contrib.auth import views as auth_views
from django.urls import path, include
from account import views as acc_views
from django.conf import settings
from django.conf.urls.static import static
from .views import faq

urlpatterns = [
    #path of the admin-page
    path('admin/', admin.site.urls),
    # letting the string empty forces django to look at an empty path at 
    # account.urls. Since there is an path with emtpy strings as well, 
    # the first page displays "Login Seite"
    # login path -> class based views from django
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
    # logout path -> class based views from django
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    # register path
    path('login/', include('account.urls')),
    path('books/', include('books.urls'),name='books-site'),
     path('order/', include('order.urls'),name='order-site'),
    path('', lambda req: redirect('/books/')),
    path('faq/', faq, name='faq-site'),
    path('profile/', acc_views.profile, name='profile')
    
    
] 
handler404 = customhandler404
handler500 = customhandler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

