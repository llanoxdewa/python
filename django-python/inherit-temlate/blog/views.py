from django.shortcuts import render


def blog(req):
    data = {
        'title':'blog',
        'header':'selamat datang di blog',
        'file_css':'blog/css/style_blog.css'
    }
    return render(req,'blog/blog.html',data)
