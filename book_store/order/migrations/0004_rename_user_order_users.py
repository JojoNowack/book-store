# Generated by Django 3.2.8 on 2021-11-27 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_users_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='users',
        ),
    ]
