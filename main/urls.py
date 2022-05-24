#from django.conf.urls import url , include
from django.urls import include, re_path
from . import views


urlpatterns = [
	re_path('', views.index),
]
