from django.urls import path 
from . import views 



urlpatterns = [
    
    path("", views.HomeView.as_view(), name="home"),
    path("login/",views.LoginUser.as_view(), name="login"),
    path("logout/", views.LogoutUser.as_view(), name="logout"),
    path("register/",views.RegisterUser.as_view(), name="register"),
    path("user_profile/<str:username>/",views.UserProfile.as_view(), name="user_profile"),
    # path("search-results/",views.searchResults, name="search_results")
    path("post/<int:pk>", views.ViewPost.as_view(), name="view_post"),
    path("compose/post/", views.PostChirp.as_view(), name="post_chirp"),
    
]