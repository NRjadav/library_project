# Generated by Django 4.2 on 2024-11-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_author_timestamp_books_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_user',
            name='password_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
