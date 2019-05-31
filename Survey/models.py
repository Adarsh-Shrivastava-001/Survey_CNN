from django.db import models

# Create your models here.

class Results(models.Model):
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    neither = models.IntegerField()
