# Generated by Django 4.2 on 2024-11-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_category_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
