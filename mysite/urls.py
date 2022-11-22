
from django.contrib import admin
from django.urls import path

from my_celery.views import get_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",get_page, name='get_page')
]
