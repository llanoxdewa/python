from django.http import HttpResponse
def home(req):
    return HttpResponse("<h1 style='color:red;font-size:20px;text-align:center;'> selamat datand di web pertama saya </h1>")

def about(req):
    return HttpResponse('<h1>about</h1>')
