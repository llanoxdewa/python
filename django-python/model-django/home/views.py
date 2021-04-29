from django.shortcuts import render

def home_page(req):
    data = {
        'title':'home',
        'header':'selamat datang di home page'
    }
    return render(req,'index.html',data)
