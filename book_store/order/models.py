from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from account.models import Profile
from books.models import Book

# from account.models import Profile
# Create your models here.

class Order(models.Model):
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField()
    books = models.ForeignKey(Book, on_delete=CASCADE)
    users = models.ForeignKey(Profile, on_delete=CASCADE)
    
    def __str__(self):
        return '{book} ist entliehen von {user}'.format(book = self.books.title, user = self.users.username)
     