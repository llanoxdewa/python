from django.shortcuts import render
def home_page(req):
    data = {
        'judul' : 'home | projek1',
        'css_file' : 'home/css/style.css',
        'js_file' : 'home/js/script.js'
    }
    return render(req,'home/index.html',data)

