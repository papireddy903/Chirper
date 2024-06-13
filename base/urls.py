from django.urls import path 
from . import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", views.home_view, name="home"),
    path("login/",views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/",views.registerUser, name="register"),
    path("user_profile/<str:username>/",views.user_profile, name="user_profile"),
    # path("search-results/",views.searchResults, name="search_results")
    path("post/<int:pk>", views.view_post, name="view_post"),
]