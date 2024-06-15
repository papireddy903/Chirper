from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.hashers import make_password
from .models import Chirp,Like, CustomUser, Follow
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.http import JsonResponse  
from rest_framework_simplejwt.tokens import RefreshToken

import json 
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View


class PostChirp(View):
    def post(self, request):
        user = request.user
        
        form = ChirpForm(request.POST)
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.author = user 
            chirp.save()
            return redirect('home')
        
    def get(self, request):
        user = request.user 
        form = ChirpForm()
        return render(request, 'chirp.html', {'form':form})




# @login_required()
# def home_view(request):
#     user = request.user
#     if request.method == 'POST':
#         form = ChirpForm(request.POST)
#         if form.is_valid():
#             chirp = form.save(commit=False)
#             chirp.author = user
#             chirp.save()
#             return redirect('home')
#     else:
#         form = ChirpForm()
#     chirps = Chirp.objects.all().order_by('-created')
#     return render(request, 'home.html', {'form': form, 'chirps': chirps})

        
class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        form = ChirpForm()
        chirps = Chirp.objects.all().order_by('-created') 
        return render(request, 'home.html', {'form': form, 'chirps': chirps})

    def post(self, request):
        user = request.user 
        form = ChirpForm(request.POST)
        if form.is_valid():
            chirp = form.save(commit=False) 
            chirp.author = user
            chirp.save()
            return redirect('home')
        chirps = Chirp.objects.all().order_by('-created') 
        return render(request, 'home.html', {'form': form, 'chirps': chirps})



        


# def loginUser(request):
#     if request.method == 'POST':
#         body = json.loads(request.body)
#         email = body.get('email')
#         password = body.get('password')
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             refresh = RefreshToken.for_user(user)
#             response_data = {
#                 'access': str(refresh.access_token), 
#                 'refresh':str(refresh),
#             }

#             response = JsonResponse(response_data) 
#             response.status_code = 200 
#             return response 
#             # return redirect('home') 
#         else:
#             return JsonResponse({'detail': 'Invalid credentials'}, status=401)
#     else:
#         return render(request, "login.html", {})
    
class LoginUser(View):
    def get(self, request):
        return render(request, "login.html", {})


    def post(self, request):
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

    
# def logoutUser(request):
#     logout(request)
#     return redirect('home') 

class LogoutUser(View):
    def get(self,request):
        logout(request)
        return redirect('home')

# def registerUser(request):
#     if request.method=='POST':
#         form = CustomUserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm() 
    

#     return render(request, "register.html", {"form":form}) 


class RegisterUser(View):
    
    def get(self,request):
        form = CustomUserCreationForm()
        return render(request, "register.html", {"form":form})
    
    def post(self,request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    
        return render(request, "register.html", {"form":form})
    








# def user_profile(request,username):
#     user = get_object_or_404(CustomUser, username=username)
#     chirps = Chirp.objects.filter(author=user.id).order_by('-created')
#     return render(request, 'user_profile.html', {"user":user,"chirps":chirps})


class UserProfile(View):
    def get(self,request, username):
        user = get_object_or_404(CustomUser, username=username)
        chirps = Chirp.objects.filter(author=user.id).order_by('-created')
        return render(request, 'user_profile.html', {"user":user,"chirps":chirps})
        






def search_results(request):
    if request.method=='POST':
        query = request.POST.get('query','')

        results = Chirp.objects.filter(chirp__icontains=query)

        return render(request, "home.html", {"results":results})
    

# def view_post(request,pk):

#     chirp = Chirp.objects.get(id=pk)

#     return render(request, "view_post.html", {"chirp":chirp}) 


class ViewPost(View):
    def get(self,request, pk):
        chirp = Chirp.objects.get(id=pk)

        return render(request, "view_post.html", {"chirp":chirp}) 
