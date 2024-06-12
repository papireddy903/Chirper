from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/",views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/",views.registerUser, name="register"),
    path("user_profile/<str:username>/",views.user_profile, name="user_profile"),
    # path("search-results/",views.searchResults, name="search_results")
]