from django.contrib import admin
from .models import PostModel

class AdminModel(admin.ModelAdmin):
    readonly_fields = ['publish','update','slug']



admin.site.register(PostModel,AdminModel)



