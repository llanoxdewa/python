from django.shortcuts import render

def blog_page(req):
    data = {
        'title':'blog',
        'framework_css':'bootstrap/css/bootstrap.min.css',
        'framework_js':'bootstrap/js/bootstrap.min.js',
        'header':'welcome to my blog',
        'css':'blog/css/style.css'
    }
    return render(req,'blog/index.html',data)
