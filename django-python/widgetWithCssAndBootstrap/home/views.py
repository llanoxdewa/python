from django.shortcuts import render
from .forms import LoginForm




def index(req):
    login_form = LoginForm()
    if req.method == "POST":
        data_user = {
            'username' : req.POST['username'],
            'password' : req.POST['password'],
            'email_address' : req.POST['email_address']
        }
    else:
        data_user = False
    return render(req,'home/index.html',{
        'title' : 'home page',
        # 'file_js' : 'home/js/script.js',
        # 'file_css' : 'home/css/style.css'
        'login_form' : login_form,
        'data_user' : data_user
    })
