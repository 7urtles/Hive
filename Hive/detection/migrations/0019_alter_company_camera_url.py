# Generated by Django 3.2.2 on 2021-06-11 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0018_company_camera_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='camera_url',
            field=models.CharField(default='http://192.168.1.216/stream.mjpg', max_length=200),
        ),
    ]
