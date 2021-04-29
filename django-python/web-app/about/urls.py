from django.urls import path
from . import views

urlpatterns = [
    path('',views.about_page),
    path('pembuat/',views.profile)
]


