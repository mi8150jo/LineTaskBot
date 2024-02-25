from django.urls import path
from . import views

app_name = "webapp"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('new/', views.TaskCreateView.as_view(), name='new'),
    path('edit/<int:pk>', views.TaskUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
]