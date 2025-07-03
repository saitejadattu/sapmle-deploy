from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class MyUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
class MyTodo(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='todos', null=True)
    task = models.TextField(null=True)
    status = models.BooleanField(default=False, null=True)
    date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)





