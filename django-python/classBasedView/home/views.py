from django.shortcuts import render
from django.views.generic.base import TemplateView

# class Index(TemplateView):
#     TEMPLATE_NAME = 'home/index.html'
#     CONTEXT = {
#         'title' : 'home | page'
#     }
#     # overide method get dar parent class view
#     def get(self,request):
#         return render(request,self.TEMPLATE_NAME,self.CONTEXT)

# inharitance dari TemplateResponseMixin
# ContextMixin
# View

# membuat view menggunakan template_name nya di url
class Index(TemplateView):
    pass

# membuat context dengan get_context_data
class ContextView(TemplateView):
    template_name = 'home/context.html'

    def get_context_data(self):
        return {
            'title' : 'context page view',
            'penulis' : 'llano van dewa'
        }

# mengambil parameter dari url
class ParameterView(TemplateView):
    template_name = 'home/parameter.html'

    def get_context_data(self,*args,**kwargs):
        context = kwargs
        context['title'] = 'ParameterView'
        return context
