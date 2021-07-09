from django.urls import path
from . import views


urlpatterns = [
    path('',views.blog_page),
    path('program_lmp_mrh/',views.blog_program_lampu_merah)
]

