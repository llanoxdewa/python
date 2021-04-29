from django.shortcuts import render


def homePage(req):
    data = {
        'title':'home',
        'header':'selamat datang di home page',
        'nama':'llano kusuma dewa',
        'status':'pelajar'
    }
    return render(req,'home/index.html',data)

def homePageAbout(req):
    data = {
        'title':'About',
        'nama':'llano kusuma dewa',
        'sekolah':'SMKN 1 Gunung Putri',
        'umur':'17 thn',
        'nav':[
           [1,'llano'],
           [2,'ujang'],
           [3,'tatang'],
           [4,'rizki']
        ]
    }
    return render(req,'home/about.html',data)


