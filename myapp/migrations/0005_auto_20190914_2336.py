# Generated by Django 2.2.1 on 2019-09-14 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190914_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(default='bandup/media/default.jpg', upload_to='profile_pics'),
        ),
    ]
