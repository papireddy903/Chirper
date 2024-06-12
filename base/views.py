from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *

from django.shortcuts import get_object_or_404


def home_view(request):
    user = request.user
    if request.method == 'POST':
        form = ChirpForm(request.POST)
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.author = user
            chirp.save()
            return redirect('home')
    else:
        form = ChirpForm()
    chirps = Chirp.objects.all().order_by('-created')
    return render(request, 'home.html', {'form': form, 'chirps': chirps})

        


        


def loginUser(request):
    if request.method=='POST':
        email = request.POST['email']
        # user = CustomUser.objects.get(email=email)
        # print(user.password)
        password = request.POST['password'] 
        # print(password)
# 
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
 
        else:
            print('login failed')
            return redirect('login')
    else:
        return render(request, "login.html", {})
    
def logoutUser(request):
    logout(request)
    return redirect('home') 

def registerUser(request):
    pass 

def user_profile(request,username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'user_profile.html', {"user":user})

def search_results(request):
    if request.method=='POST':
        query = request.POST.get('query','')

        results = Chirp.objects.filter(chirp__icontains=query)

        return render(request, "home.html", {"results":results})
    