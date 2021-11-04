from django.contrib import admin
from django.urls import path, include
from account.views import loginView

urlpatterns = [
    path('login', loginView, name="login")
]
