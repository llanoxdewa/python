from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    email = models.EmailField(default='nama@gmail.com')
    alamat = models.CharField(max_length=255,blank=True)
    waktu_posting = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.email}'




