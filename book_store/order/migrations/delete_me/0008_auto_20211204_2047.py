# Generated by Django 3.2.8 on 2021-12-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_book_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='borrow_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='return_date',
            field=models.DateField(),
        ),
    ]