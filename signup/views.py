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

class DogList(APIView):
  def post(self, request, format=None):
    serializer = DogSerialzer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
  def post(self, request, format=None):
    dog = get_object_or_404(Dog, pk=request.data["dog"]["dog_id"])
    userdata = request.data["user"]
    user = User.objects.create(username=userdata["email"], email=userdata["email"], password=userdata["password"])
    dog.user = user
    dog.save()
    serializer = UserSerializer(instance=user)

    return Response(serializer.data, status=status.HTTP_201_CREATED)





# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
