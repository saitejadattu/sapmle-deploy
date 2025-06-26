from rest_framework import serializers
from .models import myUser

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = "__all__" 
