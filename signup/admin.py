from django.contrib import admin

# Register your models here.
from .models import DogBreed, Dog

admin.site.register(DogBreed)
admin.site.register(Dog)
