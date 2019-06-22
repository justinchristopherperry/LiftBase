from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url

from programs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^programs/(\d+)/', views.program_detail, name='program_detail'),
]
