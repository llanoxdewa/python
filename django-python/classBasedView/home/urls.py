from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

app_name = 'home'


urlpatterns = [
    path('',Index.as_view(template_name='home/index.html'),name='index'),
    path('default',TemplateView.as_view(template_name='home/index2.html')),
    path('context',ContextView.as_view()),
    path('parameter/<slug:inputan>',ParameterView.as_view())
]

"""
1. jika suatu halaman statis / tidak berubah isinya maka
langsung gunakan TemplateView.as_view(param)

2.
"""
