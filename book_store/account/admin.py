from django.contrib import admin
from .models import Post, Profile

# Register your models here.
# add the option for the admin, to have access to the data base manipulation
admin.site.register(Post)
admin.site.register(Profile)
