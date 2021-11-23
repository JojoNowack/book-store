#from account.models import Author
from django.db import models
#from account.models import Author
# from account.models import Author
# Create your models here.

# DB-model for Book
class Book(models.Model):
    book_img = models.ImageField(default = 'book.jpg', upload_to='book_pics')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    # date = models.DateTimeField() 
    isavailable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title