from django.urls import path
from . import views

urlpatterns = [
    path('res', views.fun)
]