from django.conf.urls import url

from githubApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^profile/$', views.profile, name='test'),

]
