from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('<str:fil>',views.home_page),
]



