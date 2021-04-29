# views about

from django.shortcuts import render
from django.http import HttpResponse


def about_page(req):
    return render(req,'about/about_page.html')


def profile(req):
    return HttpResponse("<h1> LLANO KUSUMA DEWA </h1>")

