# Generated by Django 4.2 on 2024-11-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_books_book_language_remove_books_book_languages_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='book_language',
        ),
        migrations.AddField(
            model_name='books',
            name='language_data',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.language'),
        ),
        migrations.RemoveField(
            model_name='books',
            name='book_languages',
        ),
        migrations.AddField(
            model_name='books',
            name='book_languages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
