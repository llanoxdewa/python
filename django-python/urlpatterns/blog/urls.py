from django.urls import path
from . import views
urlpatterns = [
    path('/',views.blog_page),
    # path('/<str:categoryInput>',views.categoryPost),
    path('/post/<slug:slugInput>',views.singlePost)
]


