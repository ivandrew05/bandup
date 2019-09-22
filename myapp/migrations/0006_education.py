# Generated by Django 2.2.1 on 2019-09-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190914_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_image', models.ImageField(default='bandup/media/default.jpg', upload_to='profile_pics')),
                ('teacher_name', models.CharField(max_length=100)),
                ('years_of_playing', models.CharField(max_length=100)),
                ('course_content', models.CharField(max_length=5000)),
                ('charging_fee', models.CharField(max_length=100)),
            ],
        ),
    ]