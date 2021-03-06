# Generated by Django 2.2.1 on 2019-06-05 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0008_storedata_mac_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('files', models.FileField(upload_to='files/%Y/')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
