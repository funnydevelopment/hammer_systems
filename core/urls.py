from django.urls import path
from core import views


urlpatterns = [
    path("api/user_auth/", views.UserCreateAPI.as_view()),
    path("api/user_auth/check_code/", views.UserCheckCodeAPI.as_view()),
    path("api/profile/", views.UserProfileAPI.as_view()),
]
