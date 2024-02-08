from django.db import models

# Create your models here.
class Task(models.Model):
    user_ID = models.CharField(max_length=255, primary_key=True)
    content = models.TextField()
    date = models.DateTimeField()