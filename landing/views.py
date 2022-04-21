from django.shortcuts import render
from news.models import News, Tag

def index(request):
    news = News.objects.all()
    tags = Tag.objects.all()
    return render(request, 'landing/index.html', {
        'news': news,
        'tags': tags
    })

def filter(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    news = tag.news_set.all()
    return render(request, 'landing/index.html', {
        'news': news,
        'tags': Tag.objects.all()
    })