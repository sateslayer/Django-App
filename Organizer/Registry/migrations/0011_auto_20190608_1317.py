# Generated by Django 2.2.1 on 2019-06-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0010_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='allowedUsers',
            field=models.CharField(default='', max_length=1000, verbose_name='Allowed Users: '),
        ),
        migrations.AddField(
            model_name='storedata',
            name='batch_number',
            field=models.IntegerField(default=0, verbose_name='Batch number'),
        ),
    ]
