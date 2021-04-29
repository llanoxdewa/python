from django.shortcuts import render

def loginPage(req):
    data = {
        'title':'login-page',
        'header':'selamat datang di login page',
        'fileG':"login/img/pemandangan-laut-es.png",
        'fileCss':"login/css/style.css"
    }
    return render(req,'login/index.html',data)
