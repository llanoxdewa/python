from django.db import models
import random

class Register(models.Model):

    username = models.CharField(max_length=20,default=f"person{random.randint(1,1000)}") # varchar
    email = models.EmailField()
    password = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"

# option pada object model


