from django.urls import path
from profile_manager.views import register, login

urlpatterns = [
    path('register', register),
    path('login', login)
]



