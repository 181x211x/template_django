from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class message(models.Model):
    message_text = models.CharField(max_length=200) #文字列
    pub_date = models.DateTimeField('date published') #日付
