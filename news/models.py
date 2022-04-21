from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
class News(models.Model):
    STATUS = [
        ('published', 'Published'),
        ('unpublished', 'Unpublished')
    ]
    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', null=True, blank=True, default=None)
    status = models.CharField(max_length=255, choices=STATUS, default="published")
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(verbose_name = "Дата создание", auto_now_add=timezone.now())
    
    def __str__(self):
        return f'Новость: {self.title}'

    def get_absolute_url(self):
        return reverse("details", args=[self.id])
    
    class Meta: 
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Tag(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(verbose_name="Слаг", db_index=True, max_length=255)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'Тег: {self.title}'

