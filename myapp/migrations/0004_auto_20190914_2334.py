# Generated by Django 2.2.1 on 2019-09-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190722_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(default='bandup/media/team1.png', upload_to='profile_pics'),
        ),
    ]
