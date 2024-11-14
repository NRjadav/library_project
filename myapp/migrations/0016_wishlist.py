# Generated by Django 4.2 on 2024-11-14 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_add_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.BooleanField(default=False)),
                ('book_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.books')),
                ('user_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login_user')),
            ],
        ),
    ]
