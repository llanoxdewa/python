from django.shortcuts import render


def blog_page(req):
    data = {
        'title' : 'blog | projek1',
        'css_file' : 'blog/css/style.css',
        'js_file' : 'blog/js/script.js'
    }
    return render(req,'blog/index.html',data)

def blog_program_lampu_merah(req):
    data = {
        'title' : 'program lampu merah',
        'css_file' : 'blog/program_lampu_merah/css/style.css',
        'js_file' : 'blog/program_lampu_merah/js/script.js'
    }
    return render(req,'blog/template/program_lampu_merah/index.html',data)


