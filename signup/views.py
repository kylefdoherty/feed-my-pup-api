from signup.models import DogBreed, Dog
from django.contrib.auth.models import User
from signup.serializers import DogBreedSerialzer, DogSerialzer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from IPython import embed

class DogBreedList(APIView):
  def get(self, request, format=None):
    breeds = DogBreed.objects.all()
    serializer = DogBreedSerialzer(breeds, many=True)
    return Response(serializer.data)

class UserSignup(APIView):
  def post(self, request, format=None):
    # couldn't get a writable nested serializer to work
    # for some reason it was saving the username as blank everytime
    # event though it was coming in in the request correctly. If had
    # more time would figure out how to drop into the serializer model that
    # is saving the object and debug

    user_data = request.data["user"]
    dog_data = request.data["dog"]
    user = User.objects.create(email=user_data["email"], username=user_data["email"], password=user_data["password"])
    dog = Dog.objects.create(name=dog_data["name"],
                             age=dog_data["age"],
                             gender=dog_data["gender"],
                             breed=dog_data["breed"],
                             weight=dog_data["weight"],
                             body_composition=dog_data["body_composition"],
                             activity_level=dog_data["activity_level"],
                             user=user)
    serializer = UserSerializer(instance=user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
