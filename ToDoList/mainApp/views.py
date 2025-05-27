from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

#CRUD OPERATIONS

#READ
class ListToDo(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerialize

#UPDATE
class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerialize

#CREATE
class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerialize

#DELETE
class DeleteToDo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerialize
