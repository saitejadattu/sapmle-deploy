from rest_framework import serializers
from .models import myUser,MyTodo

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = "__all__" 
class MyTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTodo
        fields = "__all__"