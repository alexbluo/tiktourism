# Generated by Django 4.1.7 on 2023-03-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tikrest', '0002_restaurant_image_alter_restaurant_time_spent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.CharField(max_length=160),
        ),
    ]
