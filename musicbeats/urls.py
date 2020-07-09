from django.urls import path
from .import views

urlpatterns = [
    path('', views.songs, name='songs'),
    path('songs/', views.songs_list, name='songs_list'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    
]
