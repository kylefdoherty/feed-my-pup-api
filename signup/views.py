from django.shortcuts import render
from rest_framework import generics
from signup.serializers import DogBreedSerialzer
from signup.models import DogBreed

class DogBreedList(generics.ListCreateAPIView):
  queryset = DogBreed.objects.all()
  serializer_class = DogBreedSerialzer
