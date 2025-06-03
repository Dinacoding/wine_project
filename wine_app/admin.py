from django.contrib import admin
from .models import WinePost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(WinePost) 
class WinePostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'wine_name', 'vintage_year', 'created_on', 'status')
    search_fields = ('title', 'wine_name')
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
