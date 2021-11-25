from django.db import models

# Create your models here.

class Book(models.Model):
    book_img = models.ImageField(default = 'book.jpg', upload_to='book_pics')
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=2000)
    year = models.DateTimeField()
    book_author = models.CharField(max_length=30)
    isavailable = models.BooleanField()
    quantity = models.IntegerField()
    genre = models.CharField(max_length=12)
    pages = models.IntegerField()

    def __str__(self):
        return self.title