from django.contrib import admin
from .models import Post

class AdminSite(admin.ModelAdmin):
    readonly_field = ['post_time','update']


admin.site.register(Post,AdminSite)


