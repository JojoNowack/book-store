from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=2000)
    date = models.DateTimeField()
    author = models.CharField(max_length=30)
    isavailable = models.BooleanField()