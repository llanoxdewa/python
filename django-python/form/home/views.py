from django.shortcuts import render
from .forms import LoginForm



def index(req):
    login_form = LoginForm()
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
    else:
        username = None
        password = None
    return render(req,'home/index.html',{
        'judul' : 'home page',
        'heading' : 'selamat datang di home page',
        'data' : {
            'username' : username,
            'password' : password
        },
        'file_js' : 'home/js/script.js',
        'login_form' : login_form
    })
