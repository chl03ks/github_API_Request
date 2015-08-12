from django.conf.urls import url

from githubApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
