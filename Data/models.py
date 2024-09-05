from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tasks(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)