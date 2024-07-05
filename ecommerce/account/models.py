from django.db import models
from django.contrib.auth.models import User
from product.models import product



# Create your models here.
class login_page(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user
