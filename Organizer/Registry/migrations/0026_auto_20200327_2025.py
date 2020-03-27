# Generated by Django 3.0.4 on 2020-03-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0025_auto_20200327_1849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fileupload',
            options={'ordering': ('-upload_time', 'fileName')},
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='uploadedFile',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='fileName',
            field=models.CharField(default='temp.txt', max_length=1000),
        ),
    ]
