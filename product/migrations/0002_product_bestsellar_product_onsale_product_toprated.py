# Generated by Django 4.2.1 on 2023-05-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bestsellar',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='onsale',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='toprated',
            field=models.BooleanField(default=True),
        ),
    ]
