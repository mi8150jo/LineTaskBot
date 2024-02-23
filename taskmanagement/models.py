from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user_ID = models.CharField(max_length=32)
    content = models.TextField()
    date = models.DateField()
    startTime = models.TimeField(null=True)
    endTime = models.TimeField(null=True)
    remind_date = models.DateField(null=True)