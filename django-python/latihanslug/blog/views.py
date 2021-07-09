from django.shortcuts import render
from .models import Post


def blog_page_all(req):
    posts = [{
        'judul':post.judul,
        'slug' : post.slug,
        'publish_time' : post.publish_time,
        'body' : post.body
    } for post in Post.objects.all()]
    # category yang kece
    categorys = [p['category'] for p in Post.objects.values('category').distinct()] + ['all']
    return render(req,'blog/index.html',{
        'title' : 'blog',
        'file_css' : 'blog/css/style.css',
        'posts' : posts,
        'all' : True,
        'categorys' : categorys,
        'HOME_DIR' : 'http://localhost:8000'
    })

def blog_single_post(req,input_slug):
    post = Post.objects.get(slug=input_slug)
    return render(req,'blog/index.html',{
        "title" : f'{post.judul}',
        'post' : post,
        'file_css' : 'blog/single_post/css/style.css',
        'singlePost' : True,
        'HOME_DIR' : 'http://localhost:8000'
    })

def blog_category_post(req,input_category):
    posts = [{
        'judul':post.judul,
        'slug' : post.slug,
        'publish_time' : post.publish_time,
        'body' : post.body
    } for post in Post.objects.filter(category=input_category)]
    # category arr
    categorys = [p['category'] for p in Post.objects.values('category').distinct()] + ['all']

    return render(req,'blog/index.html',{
        'title' : f'category: {input_category}',
        'posts' : posts,
        'categoryPost' : True,
        'categorys' : categorys,
        'HOME_DIR' : 'http://localhost:8000'
    })
