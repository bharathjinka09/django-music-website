from django.urls import path
from .import views

urlpatterns = [
    path('', views.songs, name='home'),
    path('songs/', views.songs_list, name='songs_list'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup, name='signup'),
    
]
