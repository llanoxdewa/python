from django.shortcuts import render

def blog_page(req):
    return render(req,'blog/index.html')







