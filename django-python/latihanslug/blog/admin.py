from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'update_time',
        'publish_time'
    ]


admin.site.register(Post,PostAdmin)


