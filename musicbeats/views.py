from django.shortcuts import render
from musicbeats.models import Song

def songs(request):
	songs = Song.objects.all()
	return render(request, 'musicbeats/index.html', {'songs':songs})

def songs_list(request):
	songs = Song.objects.all()
	return render(request, 'musicbeats/songs.html', {'songs':songs})

def songpost(request,id):
	songpost = Song.objects.get(song_id=id)
	return render(request, 'musicbeats/songpost.html', {'songpost':songpost})

def login(request):
	return render(request, 'musicbeats/login.html')


def signup(request):
	return render(request, 'musicbeats/signup.html')
