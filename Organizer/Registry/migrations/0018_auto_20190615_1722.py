# Generated by Django 2.2.1 on 2019-06-15 11:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0017_auto_20190615_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 15, 11, 52, 36, 129026, tzinfo=utc), verbose_name='Date Posted: '),
        ),
    ]
