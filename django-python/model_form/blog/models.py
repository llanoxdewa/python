from django.db import models
from django.utils.text import slugify
from .validators import validate_judul


class PostModel(models.Model):
    # list for category
    LIST_CATEGORY = [
        ('berita','Berita'),
        ('gosip','Gosip'),
        ('olahraga','Olahraga')
    ]
    judul = models.CharField(max_length=20,validators=[validate_judul])
    body = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=LIST_CATEGORY,
        default='olahraga'
    )
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,editable=False)

    def __str__(self):
        return f"{self.id}. {self.judul}"

    def save(self):
        self.slug = slugify(self.judul)
        super(PostModel,self).save()

