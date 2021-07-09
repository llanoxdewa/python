from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostForm


def index(request):
    data_base = PostModel.objects.all()
    return render(request,'blog/index.html',{
        'title' : 'blog page',
        'data_base' : data_base,
        'file_css' : 'blog/css/style.css'
    })


def create(request):
    form_model = PostForm(request.POST or None)
    error = None
    if request.method == "POST":
        if form_model.is_valid():
            form_model.save()
            return redirect('blog:index')
        else:
            error = form_model.errors
    print(error)
    return render(request,'blog/create.html',{
        'title' : 'create blog page',
        'form_model' : form_model,
        'error_message' : error
    })


def single_post(request,slugInput):
    data_post = PostModel.objects.get(slug=slugInput)
    return render(request,'blog/single_post.html',{
        'title' : 'single post page',
        'data_post' : data_post
    })



