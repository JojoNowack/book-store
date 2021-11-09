# account -> urls

from django.urls import path
from . import views

# urlpatterns = [
#     path('login', loginView, name="login")
# ]
urlpatterns = [
    # the first page you see
    path('', views.home, name='login-site'),
    path('register/', views.register, name='register-site'),
    path('about/', views.about, name='about-site')
]