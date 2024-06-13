from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.http import JsonResponse  
from rest_framework_simplejwt.tokens import RefreshToken

import json 



@login_required()
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
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body.get('email')
        password = body.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response_data = {
                'access': str(refresh.access_token), 
                'refresh':str(refresh),
            }

            response = JsonResponse(response_data) 
            response.status_code = 200 
            return response 
            # return redirect('home') 
        else:
            return JsonResponse({'detail': 'Invalid credentials'}, status=401)
    else:
        return render(request, "login.html", {})
    
def logoutUser(request):
    logout(request)
    return redirect('home') 

def registerUser(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm() 
    

    return render(request, "register.html", {"form":form}) 

def user_profile(request,username):
    user = get_object_or_404(CustomUser, username=username)
    chirps = Chirp.objects.filter(author=user.id).order_by('-created')
    return render(request, 'user_profile.html', {"user":user,"chirps":chirps})

def search_results(request):
    if request.method=='POST':
        query = request.POST.get('query','')

        results = Chirp.objects.filter(chirp__icontains=query)

        return render(request, "home.html", {"results":results})
    

def view_post(request,pk):

    chirp = Chirp.objects.get(id=pk)

    return render(request, "view_post.html", {"chirp":chirp}) 
