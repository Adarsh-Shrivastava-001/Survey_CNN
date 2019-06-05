from django.db import models

from django.contrib.auth.models import User


class MyUser(models.Model):
    mid=models.AutoField(primary_key=True)
    e_mail=models.EmailField()
    name=models.CharField(max_length=30)
    part = models.CharField(max_length=1000)
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    neither = models.IntegerField()
    rel_corr= models.IntegerField()
    rel_wrong = models.IntegerField()

# Create your models here.

class Results(models.Model):
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    neither = models.IntegerField()
