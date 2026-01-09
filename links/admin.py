from django.contrib import admin
from .models import PageLink

@admin.register(PageLink)
class PageLinkAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'slug', 'title')
    prepopulated_fields = {'slug': ('page_name',)}
