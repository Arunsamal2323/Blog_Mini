# Generated by Django 5.0 on 2024-01-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='default_image.jpg', upload_to='images/'),
        ),
    ]
