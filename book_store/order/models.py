from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
# from account.models import Profile flasch, das ist nur die Tabelle in der die Profilbilder gespeichert werden
from books.models import Book
from django.contrib.auth.models import User

# from account.models import Profile
# Create your models here.


class Order(models.Model):
    borrow_date = models.DateField()
    return_date = models.DateField()
    books = models.ForeignKey(Book, on_delete=CASCADE)
    users = models.ForeignKey(User, on_delete=CASCADE)
    book_borrowed = models.BooleanField()
    
    def __str__(self):
        return '{book} ist entliehen von {user}'.format(book = self.books.title, user = self.users.username)


class collection(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    temp_number = models.IntegerField()
    all_orders = models.CharField(max_length=1000)