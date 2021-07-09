from django.db import models


class Instagram(models.Model):
    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(default="your@gmail.com")
    create_date = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.id}. {self.username}"
