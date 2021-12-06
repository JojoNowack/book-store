# Generated by Django 3.2.8 on 2021-12-06 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0013_auto_20211206_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='author',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='body',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='date',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='isavailable',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='title',
        ),
        migrations.AddField(
            model_name='collection',
            name='all_orders',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='temp_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
