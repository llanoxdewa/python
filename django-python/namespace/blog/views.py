from django.shortcuts import render

def blog_page(req):
    return render(req,'blog/index.html',{
        'judul' : 'home page blog'
    });

def single(req):
    return render(req,'blog/index.html',{
        'judul' : 'single page blog'
    });

def category(req):
    return render(req,'blog/index.html',{
        'judul' : 'category page blog'
    });

def input(req,input):
    return render(req,'blog/index.html',{
        'judul' : input
    });



