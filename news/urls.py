from django.urls import path
from news import views

urlpatterns = [
    path('', views.NewsCreate.as_view(), name="news"),
    path('<int:id>', views.NewsDetails.as_view(), name="details"),
    path('<int:id>/delete', views.NewsDelete.as_view(), name="delete"),
    path('<int:id>/edit', views.UpdateView.as_view(), name="edit")
]