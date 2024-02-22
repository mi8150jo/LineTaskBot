from django.urls import path
from . import views

app_name = "taskmanagement"

urlpatterns = [
    path('', views.index, name='taskmanagement'),
]