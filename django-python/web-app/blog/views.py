# views for blog
from django.shortcuts import render


def home_blog(req):
    return render(req,'blog/home_blog.html')

def recent(req):
    return render(req,'blog/recent-blog.html')


