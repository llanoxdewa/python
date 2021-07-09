from django.shortcuts import render
from .forms import ContactForm



def index(req):
    contact_form = ContactForm()
    print(req.POST)
    if req.method == 'POST':
        # tombol = req.POST['tombol']
        nama_lengkap = req.POST['nama']
        umur = req.POST['umur']
        gender = req.POST['gender']
        tanggal_lahir = {
            'tanggal' : req.POST['tanggal_lahir_day'],
            'bulan' : req.POST['tanggal_lahir_month'],
            'tahun' : req.POST['tanggal_lahir_year']
        }
        alamat = req.POST['alamat']
    else:
        nama_lengkap = umur = gender = tanggal_lahir = alamat = tombol = None
    print(tanggal_lahir)
    return render(req,'contact/index.html',{
        'title' : 'contact page',
        'contact_form' : ContactForm,
        # 'file_js' : 'home/js/script.js',
        # 'file_css' : 'home/css/style.css',
        'data_user' : {
            'nama_lengkap' : nama_lengkap,
            'umur' : umur,
            'gender' : gender,
            'tanggal_lahir' : tanggal_lahir,
            'alamat' : alamat
            # 'tombol' : tombol
        }
    })
