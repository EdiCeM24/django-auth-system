


from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static
from django.contrib.staticfiles import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edimars.urls')),
]

