# Generated by Django 3.2.8 on 2021-11-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_isavailable'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(default='default.jpg', upload_to='book_pics'),
        ),
    ]
