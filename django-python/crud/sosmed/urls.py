from django.urls import path
from . import views

app_name = 'sosmed'


urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('delete/<str:user_delete>',views.delete,name='delete'),
    path('update/<str:user_update>',views.update,name='update'),
    path('delete_page/',views.delete_page,name='delete_page'),
    path('update_page/',views.update_page,name='update_page')
]








