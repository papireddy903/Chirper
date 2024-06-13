from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/',views.ProtectedView.as_view(),name='protected'),
    path("users/", views.UsersList, name='user_list'),
    path("users/<int:pk>", views.UserDetail, name='user_detail'),
    path("chirps/", views.ChirpList, name='chirp_list'),
    path("chirps/<int:pk>", views.ChirpDetail, name='chirp_detail'),
]