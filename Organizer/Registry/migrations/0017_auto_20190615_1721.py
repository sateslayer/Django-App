# Generated by Django 2.2.1 on 2019-06-15 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0016_auto_20190615_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 15, 11, 51, 27, 759224, tzinfo=utc), verbose_name='Date Posted: '),
        ),
    ]
