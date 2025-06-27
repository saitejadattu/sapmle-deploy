from django.db import models
# Create your models here.
class myUser(models.Model):
    name = models.CharField(null=True)
    age = models.IntegerField(null=True)
class MyTodo(models.Model):
    task = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

