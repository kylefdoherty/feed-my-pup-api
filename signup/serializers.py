from rest_framework import serializers
from signup.models import DogBreed, Dog

class DogBreedSerialzer(serializers.ModelSerializer):
  class Meta:
    model = DogBreed
    fields = ("name")

class DogSerialzer(serializers.ModelSerializer):
  class Meta:
    model = Dog
    field = ("name", "gender", "breed", "age", "weight", "body_composition", "activity_level")
