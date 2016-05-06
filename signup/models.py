from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DogBreed(models.Model):
  name = models.CharField(max_length=255)

class Dog(models.Model):
  name = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  age = models.IntegerField()
  breed = models.CharField(max_length=255)
  weight = models.DecimalField(max_digits=5, decimal_places=2)
  body_composition = models.CharField(max_length=255)
  activity_level = models.CharField(max_length=255)
  user = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE, null=True, blank=True, default=0) # automatically creates an index for foreign keys

# class Allergy -  probably create many_to_many relationship
  # i.e. dog can have many allergies and allergies can belong to many dogs
  # this is good because then Allergy object can have more data such as:
    # causes, remedies, common breeds effected, etc.



# usershippinginfo - zipcode, etc.
