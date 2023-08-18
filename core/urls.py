from django.urls import path
from core import views


urlpatterns = [
    path("api/user_auth/", views.UserCreateAPI.as_view()),
    # path("api/user_auth/check_code/"),
    # path("api/profile/"),
]
