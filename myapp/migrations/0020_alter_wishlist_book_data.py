# Generated by Django 4.2 on 2024-11-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_wishlist_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='book_data',
            field=models.ManyToManyField(related_name='book_data', to='myapp.books'),
        ),
    ]
