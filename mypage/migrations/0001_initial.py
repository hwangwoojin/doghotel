# Generated by Django 3.0.7 on 2020-06-11 14:50

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('breed', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('weight', models.IntegerField(blank=True, default=0)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.user')),
            ],
        ),
    ]