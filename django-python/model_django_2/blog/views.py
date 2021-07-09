from django.shortcuts import render
from .models import *

def blog_page(req):
    data_registers = Register.objects.all()
    for data_register in data_registers:
        hidepassword = str(data_register.password)
        data_register.password = hidepassword[:3] + (len(hidepassword) - 3) * '*'
        data_register.time = str(data_register.time).split(' ')[0]
    data = {
        'judul' : 'blog',
        'file_css' : 'blog/css/style.css',
        'js_file' : 'blog/js/script.js',
        'data_registers' : data_registers
    }
    return render(req,'blog/index.html',data)
