from django.urls import path
from .views import *
from django.views.generic import TemplateView,RedirectView

app_name = 'cbv'


urlpatterns = [
    # path('home',RedirectView.as_view(url='cbv:index'),name='home'),
    path('home',HomeView.as_view(),name='home'),
    path('',
        TemplateView.as_view(template_name='index.html',extra_context={'title' : 'testing page'}),
        name='index'
    ),
    path('context/<str:inputURL>',WithContext.as_view(),name='context_with_input'),
    path('model_post/<str:inputURL>',RedirectPostModel.as_view(),name='model_post'),
    path('<str:inputURL>',WithContext.as_view(),name='redirect_to_post_model'),
    path('djangodoc',RedirectView.as_view(url='https://docs.djangoproject.com/en/3.2/topics/class-based-views/'),name='django-documentasion')
]

