# Generated by Django 4.1.7 on 2023-03-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tikrest', '0005_alter_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='prox_mi',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
