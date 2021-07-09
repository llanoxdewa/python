from django.db import models
from django.utils.text import slugify

class PostModel(models.Model):
    author = models.CharField(max_length=20,blank=True)
    judul = models.CharField(max_length=50,blank=True)
    body = models.TextField(blank=True)
    category = models.CharField(
        max_length=20,
        choices=(
            ('gosip','Gosip'),
            ('berita','Berita'),
            ('Olahraga','Olahraga')
        ),
        default="perempuan"
    )
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,editable=False)

    def __str__(self):
        return f"{self.id}. {self.judul}"

    def save(self):
        self.slug = slugify(self.judul)
        super(PostModel,self).save()

