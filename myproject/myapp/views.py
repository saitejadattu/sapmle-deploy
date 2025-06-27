from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MyUserSerializer,MyTodoSerializer
from .models import myUser,MyTodo
from rest_framework import mixins, generics

@api_view(["GET", "POST"])
def getUsers(request):
    if request.method == "GET":
        users = myUser.objects.all()
        user_serializers = MyUserSerializer(users, many=True)
        return Response(user_serializers.data)
    if request.method == "POST":
        user_serializers = MyUserSerializer(data=request.data)
        if user_serializers.is_valid():
            user_serializers.save()
            return Response(user_serializers.data)
        return Response(user_serializers.errors)
    return Response(user_serializers.errors)
    

@api_view(["PUT", "DELETE"])
def updateAndDelete(request, id):
    user = myUser.objects.get(id=id)
    if request.method == "PUT":
        user_serializer = MyUserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    if request.method == "DELETE":
        user.delete()
        return Response("deleted")
    return Response(user_serializer.errors)


class UserGetAndPOST(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = myUser.objects.all()
    serializer_class = MyUserSerializer
    # def get(self,request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    # def post(self,request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    

class UserGETAndPUTAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = myUser.objects.all()
    serializer_class = MyUserSerializer
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    
class TodoGetAndPutAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyTodo.objects.all()
    serializer_class = MyTodoSerializer 
class TodoCreateAndRetrieve(generics.ListCreateAPIView):
    queryset = MyTodo.objects.all()
    serializer_class = MyTodoSerializer