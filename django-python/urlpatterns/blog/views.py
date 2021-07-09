from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def blog_page(req):
    posts = Post.objects.all()
    slugs = [str(post.slug) for post in posts]
    return render(req,'blog/index.html',{'slugs' : slugs})

# def categoryPost(req,categoryInput):
#     posts = Post.objects.filter(categoryInput)
#     data = {'posts' : posts}
#     return render(req,'blog/index.html',data)

def singlePost(req,slugInput):
    post = Post.objects.get(slug=slugInput)

    # judul = f"<h1>{post.judul}</h1>"
    # isi = f"<p>{post.isi}</p>"
    # category = f"<p>{post.category}</p>"
    # return HttpResponse(judul + '<br>' + isi + '<br>' + category)
    return render(req,'blog/single_post.html',{'post' : post})
