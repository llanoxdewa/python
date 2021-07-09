from django.db import models
from django.utils.text import slugify
class Post(models.Model):

    judul = models.CharField(max_length=50)
    isi = models.TextField()
    category = models.CharField(max_length=20)
    waktu = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super(Post,self).save()

    def __str__(self):
        return f"{self.judul}"


