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
    path('test/', views.test, name='items-site'),
    # the path to the main page 
    path('about/', views.about, name='about-site')
]