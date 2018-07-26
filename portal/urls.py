from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf.urls import handler404, handler500
urlpatterns = [
      url(r'^$', views.kaarindex , name='kaarindex'),
      url(r'^instructions$', views.instructions , name='instructions'),
      url(r'^kaarstudent$', views.kaarstudent , name='kaarstudent'),
      url(r'^kaarsignin$', views.kaarsignin , name='kaarsignin'),
      url(r'^test$', views.test , name='kaartest'),
      url(r'^endtest$', views.kaarfinish , name='endtest'),
      url(r'^karcheck$', views.karcheck , name='karcheck'),
]

# handler404 = views.error_500
# handler500 = views.error_500