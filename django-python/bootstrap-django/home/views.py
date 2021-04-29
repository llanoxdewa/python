from django.shortcuts import render


def home_page(req):
    data = {
        'title':'home',
        'framework_css':'bootstrap/css/bootstrap.min.css',
        'framework_js':'bootstrap/js/bootstrap.min.js',
        'header':'selamat datang',
        'css':'home/css/style.css'
    }
    return render(req,'home/index.html',data)


