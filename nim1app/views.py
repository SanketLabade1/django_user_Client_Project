from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from .serializer import Userserializer,Clientserializer,Projectserializer
from rest_framework import viewsets
from .models import User, Clients,Project

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =Userserializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = Clientserializer 
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = Projectserializer  
    



