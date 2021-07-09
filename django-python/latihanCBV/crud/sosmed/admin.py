from django.contrib import admin
from .models import Instagram


class AccountData(admin.ModelAdmin):
    readonly_fields = [
        'create_date',
        'update'
    ]


admin.site.register(Instagram,AccountData)




