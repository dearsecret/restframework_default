from django.urls import path
from . import views

urlpatterns = [
    path("jwt-login", views.JWTLogin.as_view()),
]
