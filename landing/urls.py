from django.urls import path 
from landing import views

urlpatterns = [
    path('', views.index),
    path('filter/<slug:tag_slug>', views.filter, name="news.filter")
]
