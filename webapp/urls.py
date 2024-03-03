from django.urls import path
from . import views

app_name = "webapp"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('new/', views.TaskCreateView.as_view(), name='new'),
    path('edit/<int:pk>', views.TaskUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
    path('pastTask/', views.pastTask, name='pastTask'),
    path('task_detail/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('new_pastTask/', views.PastTaskCreateView.as_view(), name='new_pastTask'),
]
