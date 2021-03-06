# Generated by Django 2.2.1 on 2019-05-31 12:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=3000, verbose_name='Message: ')),
                ('datePosted', models.DateTimeField(auto_now_add=True, verbose_name='Date Posted: ')),
                ('allowedUsers', models.CharField(max_length=1000, verbose_name='Allowed Users: ')),
            ],
            options={
                'ordering': ('-datePosted',),
            },
        ),
        migrations.CreateModel(
            name='storeData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=100, verbose_name='Student Name')),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be of the form: 9876543210.', regex='^[0-9]{10}$')], verbose_name='Phone Number')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('no_of_class_attended', models.IntegerField(default=0)),
                ('fee_status', models.BooleanField(default=False)),
                ('validated', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_logged_in', models.BooleanField(default=False, verbose_name='Logged in status')),
            ],
        ),
    ]
