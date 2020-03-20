from django.contrib import admin
from .models import News, KeyWords

admin.site.register(News, admin.ModelAdmin)
admin.site.register(KeyWords, admin.ModelAdmin)
