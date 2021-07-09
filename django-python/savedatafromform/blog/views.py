from django.shortcuts import render
from .forms import PostForm
from .models import PostModel
from django.http import HttpResponseRedirect


def index(req):
    post_model = PostModel.objects.all()
    # print(post_model)
    return render(req,'blog/index.html',{
        'title' : 'blog | index | myweb',
        'post_model' : post_model
    })



def create(req):
    post_form = PostForm(req.POST or None)
    error = None
    if req.method == "POST":
        if post_form.is_valid():
            PostModel.objects.create(
                judul = post_form.cleaned_data.get('judul'),
                body = post_form.cleaned_data.get('body'),
                category = post_form.cleaned_data.get('category'),
                email = post_form.cleaned_data.get('email')
            )
            return HttpResponseRedirect('/blog/')
        else:
            error = post_form.errors

    return render(req,'blog/create.html',{
        'title' : 'blog | create | myweb',
        'post_form' : post_form,
        'error_message' : error
    })


