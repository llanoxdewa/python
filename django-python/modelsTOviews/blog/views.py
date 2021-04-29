from django.shortcuts import render
from .models import Post
import logging

def blog_page(req):
    # queryset
    posts = Post.objects.all()
    logging.basicConfig(level=logging.INFO,
        format='%(asctime)s %(levelname)s -> %(message)s'
        )
    logging.info('data aman bos')
    data = {
        'title':'blog',
        'header':'welcome to blog page',
        'Posts':posts,
    }
    return render(req,'index.html',data)
