from django.contrib import admin
from .models import Blog, CustomUser

admin.site.register(Blog)
admin.site.register(CustomUser)