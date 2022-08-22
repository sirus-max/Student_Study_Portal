from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"
        
        
class DSA(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    solution = models.TextField()
    is_finished = models.BooleanField(default=FALSE)
    def __str__(self):
        return self.title
      
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=FALSE)
    def __str__(self):
        return self.title
