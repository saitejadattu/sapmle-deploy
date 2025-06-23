from django.db import models

# Create your models here.
class myUser(models.Model):
    name = models.CharField(null=True)
    age = models.IntegerField(null=True)