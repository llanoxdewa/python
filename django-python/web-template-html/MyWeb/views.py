from django.http import HttpResponse
from django.shortcuts import render

# gunakan (from django.shortcuts import render)
# render(req,<nama file>)
#            <template>


def home(req):
    return render(req,'index.html')


def artikel(req):
    return render(req,'artikel.html')
