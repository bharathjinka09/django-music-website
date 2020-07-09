from django.urls import path
from .import views

urlpatterns = [
    path('', views.songs, name='songs'),
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    
]
