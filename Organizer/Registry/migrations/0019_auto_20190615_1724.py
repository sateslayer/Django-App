# Generated by Django 2.2.1 on 2019-06-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0018_auto_20190615_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='datePosted',
            field=models.DateTimeField(verbose_name='Date Posted: '),
        ),
    ]
