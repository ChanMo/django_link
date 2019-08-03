from django.contrib import admin
from .models import *

class LinkAdmin(admin.ModelAdmin):
    list_display = ('label', 'name', 'path', 'is_active')
    list_filter = ('label', 'is_active')

admin.site.register(Link, LinkAdmin)
