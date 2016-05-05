from django.db import models

# Create your models here.
class DogBreed(models.Model):
  name = models.CharField(max_length=255)

# class Dog(models.Model):
  # name
  # age
  # breed
  # gender
  # weight
  # body comp
  # activity level
  # user_id
  # allergies (how to handle this)


# use Djnago User model

# usershippinginfo - zipcode, etc.
