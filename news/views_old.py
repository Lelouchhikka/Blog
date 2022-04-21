from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.models import News
from news.forms import NewsForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def main(request):
    news_count = News.objects.count()
    return render(request, 'news/index.html', {
        'news_count': news_count
    })

@login_required(login_url='/login')
def index(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        news = News.objects.all()
        context = {
            'news': news,
            'forms': NewsForm()
        }
        return render(request, 'news/news.html', context)

def details(request, id):
    news = News.objects.get(pk=id)
    return render(request, 'news/details.html', {
        'news': news
    })

@login_required(login_url='/login')
def edit(request, id):
    if request.method == 'GET':
        news = News.objects.get(id=id)
        form = NewsForm(instance=news)
        return render(request, 'news/edit.html', {
            'form': form
        })
    else: 
        # print(request.POST.get('title'))
        news = News.objects.get(id=id)
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news')

@login_required(login_url='/login')
def delete(request, id):
    News.objects.get(pk=id).delete()
    return redirect('news')

