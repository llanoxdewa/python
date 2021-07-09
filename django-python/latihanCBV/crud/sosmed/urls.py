from django.urls import path
from . import views
from .views import (
    SosmedHomePage,
    SosmedDeleteView
)
app_name = 'sosmed'


urlpatterns = [
    path('',SosmedHomePage.as_view(),name='index'),
    path('create/',views.create,name='create'),
    path('delete/<str:user_delete>',SosmedDeleteView.Delete.as_view(),name='delete'),
    path('update/<str:user_update>',views.update,name='update'),
    path('delete_page/',SosmedDeleteView.DeletePage.as_view(),name='delete_page'),
    path('update_page/',views.update_page,name='update_page')
]








