from django.shortcuts import render, redirect
from musicbeats.models import Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages

def songs(request):
	songs = Song.objects.all()
	return render(request, 'musicbeats/index.html', {'songs':songs})

def songs_list(request):
	songs = Song.objects.all()
	return render(request, 'musicbeats/songs.html', {'songs':songs})

def songpost(request,id):
	songpost = Song.objects.get(song_id=id)
	return render(request, 'musicbeats/songpost.html', {'songpost':songpost})


def signup(request):
	if request.method == 'POST':
		email = request.POST['email']
		username = request.POST['username']
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if User.objects.filter(username=username).exists():
			messages.error(request,"Username already exists.")
			return redirect('signup')

		elif User.objects.filter(email=email).exists():
			messages.error(request,"Email already exists.")
			return redirect('signup')

		elif password1 != password2:
			messages.error(request,"Passwords Doesn't match. Please check.")
			return redirect('signup')
			
		else:
			myuser = User.objects.create_user(username,email,password1)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.save()
			messages.success(request,"Registered successfully!")

			return redirect('login')

	return render(request, 'musicbeats/signup.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		myuser = authenticate(username=username,password=password)
		auth_login(request,myuser)
		messages.success(request, 'Logged in successfully!')
		return redirect('home')

	return render(request, 'musicbeats/login.html')

def logout_user(request):	
	logout(request)	
	messages.success(request, 'Logged out successfully!')

	return render(request, 'musicbeats/login.html')
