from django.shortcuts import render,redirect
from .forms import FormInstagram
from .models import Instagram
from django.views.generic import View,TemplateView,RedirectView

class ObjectFromModel:
    def all_data(self):
        instagram_objects_all = Instagram.objects.all()
        return instagram_objects_all

    def get_data_by_id(self,user_id):
        instagram_objects_get_by_id = Instagram.objects.get(id=user_id)
        return instagram_objects_get_by_id



class SosmedHomePage(TemplateView,ObjectFromModel):
    template_name = 'sosmed/index.html'

    def get_context_data(self,*args,**kwargs):
        context = super(SosmedHomePage,self).get_context_data(*args,**kwargs)
        context['instagram_data'] = self.all_data()
        context['title'] = 'sosmed page | home'
        context['remove_data'] = False
        return context


class SosmedDeleteView:

    class DeletePage(TemplateView,ObjectFromModel):
        template_name = 'sosmed/index.html'

        def get_context_data(self):
            context = super(SosmedDeleteView.DeletePage,self).get_context_data()
            context['title'] = 'sosmed page | delete page'
            context['instagram_data'] = self.all_data()
            context['remove_data'] = True
            return context

    class Delete(RedirectView,ObjectFromModel):
        pattern_name = 'sosmed:index'
        permanent = False
        query_string = False

        def get_redirect_url(self,*args,**kwargs):
            # Instagram.objects.get(id=kwargs['user_delete']).delete()
            self.get_data_by_id(kwargs['user_delete']).delete()
            return super(SosmedDeleteView.Delete,self).get_redirect_url()


# class SosmedFormView(View):

#     template_name = 'sosmed/create.html'
#     form = None
#     context = {}

#     def get(self,*args,**kwargs):



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
        'email' : akun_to_update.email,
        'status' : akun_to_update.status
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


