# Generated by Django 3.2.2 on 2021-05-20 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0011_entrance_exits'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exits',
            new_name='Exit',
        ),
    ]