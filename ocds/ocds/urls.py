# from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from ocds import views
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.lecture_list, name ='lecture_list'),
    path('lecture_play', views.lecture_play, name ='lecture_play'),
    path('detectme', views.detectme, name="detectme"),
    path('lecture_sort/', views.lecture_sort, name='lecture_sort'),
    path('check_user_info/', views.check_user_info, name='check_user_info'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)