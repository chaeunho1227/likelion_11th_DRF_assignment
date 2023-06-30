from django.urls import path
from .views import *
from . import views

app_name = 'music'
urlpatterns = [
    path('',views.album_list_create),
]