from rest_framework import serializers
from signup.models import DogBreed

class DogBreedSerialzer(serializers.ModelSerializer):
  class Meta:
    model = DogBreed
    field = ("name")
