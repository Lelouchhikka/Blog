from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.models import News
from news.forms import NewsForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#Class Based View 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
# @login_required(login_url='/login')
# def main(request):
#     news_count = News.objects.count()
#     return render(request, 'news/index.html', {
#         'news_count': news_count
#     })
class MainTemplate(LoginRequiredMixin, TemplateView):
    login_url='/login'
    template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_count"] = News.objects.count()
        return context
class NewsDetails(LoginRequiredMixin,DetailView):
    login_url='/login'
    template_name='news/details.html'
    model=News
    pk_url_kwarg='id'
class NewsCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    template_name = 'news/news.html'
    model = News
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = News.objects.all()
        context["forms"] = NewsForm()
        return context
# def details(request, id):
#     news = News.objects.get(pk=id)
#     return render(request, 'news/details.html', {
#         'news': news
#     })

# @login_required(login_url='/login')
# def edit(request, id):
#     if request.method == 'GET':
#         news = News.objects.get(id=id)
#         form = NewsForm(instance=news)
#         return render(request, 'news/edit.html', {
#             'form': form
#         })
#     else: 
#         # print(request.POST.get('title'))
#         news = News.objects.get(id=id)
#         form = NewsForm(request.POST, request.FILES, instance=news)
#         if form.is_valid():
#             form.save()
#             return redirect('news')
    
class NewsUpdate(LoginRequiredMixin,UpdateView):
    login_url='/login'
    template_name='news/edit.html'
    model=News
    pk_url_kwarg='id'
    form_class=NewsForm
class NewsDelete(LoginRequiredMixin,DeleteView):
    login_url='/login'
    model=News
    pk_url_kwarg='id'
    success_url='/news'
    def get(self,*args,**kwargs):
        return self.post(*args,**kwargs)