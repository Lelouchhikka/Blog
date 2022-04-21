from django.contrib import admin
from django.urls import path, include
from news.views import MainTemplate
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', include('landing.urls')),
    path('home/', MainTemplate.as_view(), name = "home"),
    path('admin/', admin.site.urls),
    path('', include('auth_user.urls')),
    path('news/', include('news.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
