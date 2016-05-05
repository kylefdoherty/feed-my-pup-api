from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from signup import views


urlpatterns = patterns('',
  url(r'^api/breeds$', views.DogBreedList.as_view()),
  url(r'^api/dogs$', views.DogList.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

