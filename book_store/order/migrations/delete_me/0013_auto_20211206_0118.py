# Generated by Django 3.2.8 on 2021-12-06 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_collection_temp_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='all_orders',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='temp_number',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='user',
        ),
        migrations.AddField(
            model_name='collection',
            name='author',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='body',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='date',
            field=models.DateTimeField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='isavailable',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='title',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
