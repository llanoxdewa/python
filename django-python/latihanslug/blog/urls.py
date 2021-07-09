from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('/',views.blog_page_all,name='index'),
    path('/post/<slug:input_slug>',views.blog_single_post,name='single_post'),
    path('/category/<slug:input_category>',views.blog_category_post,name='category_post')
]


