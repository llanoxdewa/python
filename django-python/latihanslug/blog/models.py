from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    judul = models.CharField(max_length=50)
    body = models.TextField()
    category = models.CharField(max_length=20)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,editable=False)

    def __str__(self):
        return f"{self.id}. {self.judul}"

    def save(self):
        self.slug = slugify(self.judul)
        super(Post,self).save()







