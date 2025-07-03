from rest_framework import serializers
from .models import MyTodo, MyUser
class MyTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTodo
        fields = "__all__"


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser 
        fields = ["username", "password", "email", "age"]
        extra_kwargs = {
            "password": {"write_only": True}  # 👈 hides password from API responses
        }

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            age=validated_data["age"]
        )
        return user