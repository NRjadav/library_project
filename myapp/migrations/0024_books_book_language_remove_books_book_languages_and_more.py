# Generated by Django 4.2 on 2024-11-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='books',
            name='book_languages',
        ),
        migrations.AddField(
            model_name='books',
            name='book_languages',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.language'),
        ),
    ]
