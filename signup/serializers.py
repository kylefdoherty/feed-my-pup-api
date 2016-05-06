from rest_framework import serializers
from signup.models import DogBreed, Dog
from django.contrib.auth.models import User

class DogBreedSerialzer(serializers.ModelSerializer):
  class Meta:
    model = DogBreed
    field = ("name")

class DogSerialzer(serializers.ModelSerializer):
  class Meta:
    model = Dog
    fields = ("id", "name", "gender", "breed", "age", "weight", "body_composition", "activity_level")

class UserSerializer(serializers.ModelSerializer):
  dogs = DogSerialzer(many=True, read_only=True)

  class Meta:
    model = User
    fields = ("id", "email", "dogs")
