from django.shortcuts import render

def home(req):
    data = {
        'title':'home',
        'header':'selamat datang di home',
        'file_css':'home/css/style_home.css'
    }
    return render(req,'home/home.html',data)
