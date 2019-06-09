from django.urls import path
from .views import current_user, UserList, ChangePasswordView

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('change_password', ChangePasswordView.as_view())
]
