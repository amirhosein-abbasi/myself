from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import index, about, contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
