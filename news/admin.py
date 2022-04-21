from django.contrib import admin
from news.models import News, Tag

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display=('title','description','author','status','created_at')
    list_filter=('title','status','created_at')
    search_fields=['titles']



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('title','slug')
    list_filter=('title','slug')
    search_fields=['titles']