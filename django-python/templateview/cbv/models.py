from django.db import models

class Post(models.Model):
    judul = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.judul}"

