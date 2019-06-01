from django.urls import path
from profile_manager.views import register

urlpatterns = [
    path('register', register)
]



