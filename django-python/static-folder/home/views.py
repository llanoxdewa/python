from django.shortcuts import render

def homePage(req):
    data = {
        'title':'home-page',
        'header':'selamat datang di home page',
        'fileG':"home/img/jalan-hutan.png",
        'fileCss':"home/css/style.css"
    }
    return render(req,'home/index.html',data)
