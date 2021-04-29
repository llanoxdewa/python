from django.shortcuts import render

def blog_page(req):
    data = {
        'title':'blog',
        'header':'selamat datang di blog page'
    }
    return render(req,'index.html',data)
