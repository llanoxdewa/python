from django.db import models

class Register(models.Model):

    username = models.CharField(max_length=15)
    password = models.CharField(max_length=25)
    jurusan = models.CharField(max_length=10,default="jurusan anda")
    email = models.EmailField()
    umur = models.IntegerField()

    def __str__(self):
        return f"{self.email}"

