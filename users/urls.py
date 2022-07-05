from django.urls import path
from . import views

urlpatterns = [
    path('res', views.fun),
    path('index', views.index),
    path('new', views.new,name="new"),
    path('master', views.master,name="master"),

]