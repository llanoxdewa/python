from django.db import models


class Register(models.Model):

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    status = models.CharField(max_length=15,default="kosong")

    def __str__(self):
        return f"{self.id}. {self.email}"
