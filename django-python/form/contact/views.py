from django.shortcuts import render
from .forms import ContactForm

def index(req):
    if req.method == "POST":
        nama = req.POST['nama']
        email = req.POST['email']
        username = req.POST['username']
        gender = req.POST['gender']
    else:
        nama = email = username = gender = False
    contact_form = ContactForm()
    return render(req,'contact/index.html',{
        'contact_form' : contact_form,
        'data' : {
            'nama' : nama,
            'email' : email,
            'username' : username,
            'gender' : gender
        }
    })
