from django.shortcuts import render,redirect
from .forms import FormInstagram
from .models import Instagram



def index(request):
    instagram_data = Instagram.objects.all()
    return render(request,'sosmed/index.html',{
        'title' : 'sosmed page | home ',
        'instagram_data' : instagram_data,
        'remove_data' : False
    })

def create(request):
    form_instagram = FormInstagram(request.POST or None)
    if request.method == "POST":
        if form_instagram.is_valid():
            form_instagram.save()
            return redirect("sosmed:index")

    return render(request,'sosmed/create.html',{
        'title' : 'sosmed page | create account',
        'form_instagram' : form_instagram
    })

# udapte method
def delete_page(request):
    instagram_data = Instagram.objects.all()
    return render(request,'sosmed/index.html',{
        'title' : 'sosmed page | delete page',
        'instagram_data' : instagram_data,
        'remove_data' : True
    })

def delete(request,user_delete):
    Instagram.objects.filter(id=user_delete).delete()
    return redirect("sosmed:index")
# for update method

def update_page(request):
    instagram_data = Instagram.objects.all()
    return render(request,'sosmed/index.html',{
        'title' : 'sosmed page | update page',
        'instagram_data' : instagram_data,
        'update_data' : True
    })


def update(request,user_update):
    akun_to_update = Instagram.objects.get(id=user_update)
    data_user_to_update = {
        'nama_depan' : akun_to_update.nama_depan,
        'nama_belakang' : akun_to_update.nama_belakang,
        'username' : akun_to_update.username,
        'password' : akun_to_update.password,
        'email' : akun_to_update.email
    }
    form_for_update = FormInstagram(request.POST or None,initial=data_user_to_update,instance=akun_to_update)
    if request.method == "POST":
        if form_for_update.is_valid():
            form_for_update.save()
            return redirect('sosmed:index')

    return render(request,'sosmed/create.html',{
        'title' : 'sosmed page | udpate account',
        'form_instagram' : form_for_update,
        'update' : True
    })


