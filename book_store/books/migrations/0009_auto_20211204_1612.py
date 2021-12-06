# Generated by Django 3.2.8 on 2021-12-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_rename_description_small_book_title_small'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='preview',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]