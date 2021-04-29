from django.shortcuts import render


def blogPage(req):
    return render(req,'blog/blog.html')

def ceritaPage(req):
    return render(req,'blog/cerita.html')
