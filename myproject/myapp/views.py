from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import MyTodoSerializer,MyUserSerializer
from .models import MyTodo
from rest_framework import mixins, generics
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.models import User


class TodoGetAndPutAndDelete(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = MyTodo.objects.all()
    serializer_class = MyTodoSerializer

class TodoCreateAndRetrieve(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = MyTodo.objects.all()
    serializer_class = MyTodoSerializer


def logout_view(request):
    logout(request)
    return redirect("http://localhost:5173/login")

@api_view(["POST"])
def register(request):
    serializer = MyUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Registration completed Successful")
    return Response(serializer.errors)



@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getUserTodos(request, user_id):
    user_todos = MyTodo.objects.filter(user=user_id)
    serializer = MyTodoSerializer(user_todos, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(["GET"])
def getTodos(request):
    return Response("todos")

