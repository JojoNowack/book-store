# Generated by Django 3.2.8 on 2021-11-29 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_ausleihtage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='description_small',
            new_name='title_small',
        ),
    ]