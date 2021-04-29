from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_blog),
    path('recent/',views.recent)
]


