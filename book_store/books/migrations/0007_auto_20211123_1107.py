# Generated by Django 3.2.8 on 2021-11-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20211123_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
