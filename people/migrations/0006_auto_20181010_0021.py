# Generated by Django 2.0.7 on 2018-10-09 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20181009_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_upload',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(upload_to='Posts'),
        ),
    ]
