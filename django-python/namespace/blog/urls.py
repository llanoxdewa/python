from django.urls import path
from . import views

# declaration namespace name
app_name = 'blog'


urlpatterns = [
    path('',views.blog_page, name="index"),
    path('/category',views.category, name="category"),
    path('/single',views.single, name="single"),
    path('/<str:input>',views.input, name="inputan")
]

from django.urls import include, path

