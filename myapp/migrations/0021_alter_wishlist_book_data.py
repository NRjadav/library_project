# Generated by Django 4.2 on 2024-11-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_wishlist_book_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='book_data',
            field=models.ManyToManyField(related_name='wishlist_data', to='myapp.books'),
        ),
    ]
