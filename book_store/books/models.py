from django.db import models
from django.db.models.deletion import CASCADE
from account.models import Author

# Create your models here.

class Category(models.Model):
    genre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.genre

class Book(models.Model):
    book_img = models.ImageField(default = 'book.jpg', upload_to='book_pics')
    title = models.CharField(max_length=50)
    title_small = models.CharField(max_length=30)
    description_small = models.TextField(max_length=700)
    description = models.TextField(max_length=10000)
    year = models.DateField()
    book_author = models.CharField(max_length=50)
    isavailable = models.BooleanField(default=True)
    quantity = models.IntegerField()
    genre = models.ManyToManyField(Category)
    pages = models.IntegerField()
    part = models.IntegerField()
    age = models.IntegerField()
    ausleihtage = models.IntegerField(default=30)
    language= models.CharField(max_length=20)
    preview=models.CharField(max_length=200,default=0)
    totalorders=models.IntegerField(default=0)


    

    def __str__(self):
        return self.title

