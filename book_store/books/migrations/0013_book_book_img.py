# Generated by Django 3.2.8 on 2021-11-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_remove_book_book_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(default='book.jpg', upload_to='book_pics'),
        ),
    ]
