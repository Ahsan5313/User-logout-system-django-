
from protfolio.settings import MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path,include

from .import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skill.urls')),
    path('auth/', include('account.urls')),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
