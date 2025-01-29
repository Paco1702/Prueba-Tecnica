from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Modelo para Usuario
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

#Modelo de tarea de usuario
class Tarea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="tareas")

    def __str__(self):
        return self.title