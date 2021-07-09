from django.shortcuts import render


def login_page(req):
    data = {
        'title' : 'blog page | projek1',
        'css_file' : 'login/css/style.css',
        'js_file' : 'login/js/script.js'
    }
    return render(req,'login/index.html',data)

