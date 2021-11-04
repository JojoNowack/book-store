# account -> urls

from django.urls import path
from . import views

# urlpatterns = [
#     path('login', loginView, name="login")
# ]
urlpatterns = [
    # the first page u see
    path('', views.home, name='login-site'),
    path('about/', views.about, name='about'),
]