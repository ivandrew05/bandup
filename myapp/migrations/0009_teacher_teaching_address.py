# Generated by Django 2.2.1 on 2019-09-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190922_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teaching_address',
            field=models.CharField(default='Shanghai', max_length=1000),
        ),
    ]
