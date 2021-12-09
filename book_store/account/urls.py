# account -> urls

from django.urls import path
from . import views

# urlpatterns = [
#     path('login', loginView, name="login")
# ]
urlpatterns = [
    # the first page you see
    path('login/', views.login, name='login-site'),
    path('register/', views.register, name='register-site'),
    path('test/', views.showmybooks, name='items-site'),
    # the path to the main page 
    path('about/', views.about, name='about-site'),
    path('books/', views.about, name='books-site'),
    path('faq/', views.about, name='faq-site'),
    path('', views.login, name='login-leer') #wird gebraucht damit wir nicht bei login/login landen
]