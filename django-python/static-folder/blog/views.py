from django.shortcuts import render

def blogPage(req):
    data = {
        'title':'blog-page',
        'header':'selamat datang di blog page',
        'fileG':"blog/img/jalan-hutan.png",
        'fileCss':"blog/css/style.css"
        }
    return render(req,'blog/artikel.html',data)
