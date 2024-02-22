from django.urls import path
from . import views

app_name = "webapp"

urlpatterns = [
    path('home/', views.home, name='home'),
]