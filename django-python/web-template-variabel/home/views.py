from django.shortcuts import render

def home(req):
    conteks = {
        'judul':'home',
        'pembuat':'llano van dewa',
        'header':'selamat datand di page home'
    }
    return render(req,'home/index.html',conteks)

def about(req):
    return render(req,'home/about.html')
