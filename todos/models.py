# todos/models.py
from django.db import models
from users.models import CustomUser

class Todo(models.Model):
    objects = None
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)