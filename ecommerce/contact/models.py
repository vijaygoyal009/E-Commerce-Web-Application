from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    user=models.CharField(max_length=100)
    E_mail=models.EmailField()
    massage=models.TextField()