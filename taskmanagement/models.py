from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user_ID = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()