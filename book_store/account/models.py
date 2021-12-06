from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

from books.models import Book
# from order.models import Order

# Create your models here.

class Author(models.Model): 
    author_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book)
   
    
    def __str__(self):
       return self.author_name 
    
# python-django has no attribute for profil-pictures by default
# we have to add a one:one relationship between the profile and the user
# -> one user can have one profil picture
# -> one profil picture can be used by one user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #totalorders
    #orders = models.ForeignKey(Order, on_delete=CASCADE)
    
# there could be problems if u havent installed 'pillow' 
# just install it, by downloading it via pip: pip install pillow
    def __str__(self):
        return f'{self.user.username} Profil'