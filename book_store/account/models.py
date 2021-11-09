from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# This is an example for an data base
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
# python-django has no attribute for profil-pictures by default
# we have to add a one:one relationship between the profile and the user
# -> one user can have one profil picture
# -> one profil picture can be used by one user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
# there could be problems if u havent installed 'pillow' 
# just install it, by downloading it via pip: pip install pillow
    def __str__(self):
        return f'{self.user.username} Profil'