from django.db import models

# Create your models here.
class Category(models.Model):
    genre = models.CharField(max_length=15)
    
    def __str__(self):
        return self.genre


class Book(models.Model):
    book_img = models.ImageField(default = 'book.jpg', upload_to='book_pics')
    title = models.CharField(max_length=50)
    title_small = models.CharField(max_length=30)
    description = models.TextField(max_length=2000)
    year = models.DateField()
    book_author = models.CharField(max_length=30)
    isavailable = models.BooleanField()
    quantity = models.IntegerField()
    genre = models.ManyToManyField(Category)
    pages = models.IntegerField()
    part = models.IntegerField()
    age = models.IntegerField()
    ausleihtage = models.IntegerField()
    language= models.CharField(max_length=20)
    preview=models.CharField(max_length=200,default=0)
    totalorders=models.IntegerField()

    def __str__(self):
        return self.title
    

