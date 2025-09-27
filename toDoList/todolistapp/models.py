from django.db import models

# Create your models here.
class Task (models.Model):
    task_text=models.CharField()
    is_done=models.BooleanField()
    
    def __str__(self):
        return self.task_text