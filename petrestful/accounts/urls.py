from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('token-auth/', auth_views.obtain_auth_token),
]

