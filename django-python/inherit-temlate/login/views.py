from django.shortcuts import render



def login(req):
    data = {
        'title':'login',
        'header':'selamat datang di login',
        'file_css':'login/css/style_login.css'
    }
    return render(req,'login/login.html',data)
