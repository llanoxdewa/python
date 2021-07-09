from django.shortcuts import render
from django.views import View

class Index(View):

    def get(self,request):
        return render(request,'blog/index.html',{
            'title' : 'blog'
        })

    def post(self,request):
        return render(request,'blog/index.html',{
            'title' : 'post blog page'
        })





