from django.shortcuts import render
from .models import Register
from django.http import HttpResponse
def home_page(req,fil=False):
    if(not fil):
        data_siswa = Register.objects.all()
    elif(fil not in ['elektro','las','kimia'] and fil):
        return HttpResponse('<h1 style="color:red;">jurusan tidak valid</h1>')
    else:
        data_siswa = Register.objects.filter(jurusan=fil)

    for data in data_siswa:
        data.umur = str(data.umur) + ' thn'

    data = {
        'title' : 'home page',
        'data_registers' : data_siswa,
        'file_css' : 'home/css/style.css'
    }
    return render(req,'home/index.html',data)




