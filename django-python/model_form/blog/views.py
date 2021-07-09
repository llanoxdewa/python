from django.shortcuts import render,redirect
from .forms import PostForm
from .models import PostModel
# from django.http import HttpResponseRedirect


def index(request):
    data_post_model = PostModel.objects.all()
    return render(request,'blog/index.html',{
        'title' : 'blog page',
        'data_post_model' : data_post_model
    })

def create(request):
    post_form = PostForm(request.POST or None)
    error_message = None
    if request.method == 'POST':
        if post_form.is_valid():
            # PostModel.objects.create(
            #     judul = post_form.cleaned_data.get('judul'),
            #     body = post_form.cleaned_data.get('body'),
            #     category = post_form.cleaned_data.get('category'),
            # )
            post_form.save()
            return redirect('blog:index')
        else:
            error_message = post_form.errors

    return render(request,'blog/create.html',{
        'title' : 'blog page',
        'post_form' : post_form,
        'error_message' : error_message
    })
