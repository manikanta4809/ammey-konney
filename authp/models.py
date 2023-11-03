from django.db import models

# Create your models here.
class Use(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)