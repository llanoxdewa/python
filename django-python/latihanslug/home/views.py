from django.shortcuts import render


def home_page(req):
    data = {
        'title' : 'home',
        'file_css' : 'home/css/style.css'
    }
    return render(req,'home/index.html',data)

