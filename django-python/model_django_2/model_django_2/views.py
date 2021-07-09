from django.shortcuts import render


def home_page(req):
    data = {
        'judul' : 'home',
        'file_css' : 'home/css/style.css',
        'js_file' : 'home/js/script.js'
    }
    return render(req,'home/index.html',data)






