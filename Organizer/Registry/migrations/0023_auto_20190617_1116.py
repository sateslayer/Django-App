# Generated by Django 2.2.1 on 2019-06-17 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0022_storedata_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedata',
            name='email_address',
            field=models.EmailField(default='k@g.com', max_length=254),
        ),
    ]
