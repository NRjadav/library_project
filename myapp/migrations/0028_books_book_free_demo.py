# Generated by Django 4.2 on 2024-11-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_books_book_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_free_demo',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
