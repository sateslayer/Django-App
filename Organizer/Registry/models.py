from django.db import models
#from django.utils import timezone
from django.core.validators import RegexValidator
from datetime import datetime
from pytz import timezone

class storeData(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, default = "", verbose_name = "Student Name")
    
    phone_regex = RegexValidator(regex = r'^[0-9]{10}$', message = "Phone number must be of the form: 9876543210.")
    phone_number = models.CharField(validators = [phone_regex], max_length=11, verbose_name = "Phone Number")
    batch_number = models.IntegerField(default = 0, verbose_name = "Batch number")
    
    password = models.CharField(max_length = 30, verbose_name = "Password")
    
    no_of_class_attended = models.IntegerField(default = 0)
    last_class_attended = models.DateTimeField(auto_now_add = True)
    
    last_fees_paid = models.DateTimeField(default = datetime(1970, 1, 1, tzinfo=timezone('Asia/Kolkata')))
    validated = models.BooleanField(default = False)
    
    is_superuser = models.BooleanField(default = False)
    is_logged_in = models.BooleanField(default = False, verbose_name = "Logged in status")
    unseen_message_count = models.IntegerField(default = 0)
    unseen_file_count = models.IntegerField(default = 0)
    email_address = models.EmailField()
class Message(models.Model):

    message = models.CharField(max_length = 3000, verbose_name = "Message: ")
    datePosted = models.DateTimeField(verbose_name = "Date Posted: ", default = datetime(1970, 1, 1, tzinfo=timezone('Asia/Kolkata')))
    allowedUsers = models.CharField(max_length = 1000, verbose_name = 'Allowed Users: ')
    sender = models.CharField(max_length = 100, verbose_name = 'Sender: ', default = 'admin')
   
    class Meta:
        ordering = ('-datePosted', )


class FileUpload(models.Model):
    id = models.AutoField(primary_key = True)
    description = models.CharField(blank = True, max_length = 1000)
    uploadedFile = models.FileField(upload_to = 'files/%Y/')
    upload_time = models.DateTimeField(auto_now_add = True)
    allowedUsers = models.CharField(default = "", max_length = 1000, verbose_name = 'Allowed Users: ')
    class Meta:
        ordering = ('-upload_time', )
