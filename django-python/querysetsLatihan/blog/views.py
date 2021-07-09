from django.shortcuts import render


def blog_page(req):
    data = {
        'title' : 'blog_page',
        # 'file_css' : 'blog/css/style.css'
    }
    return render(req,'blog/index.html',data)


