# Generated by Django 3.0.7 on 2020-06-12 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0005_reservation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reservation',
            new_name='reservations',
        ),
    ]
