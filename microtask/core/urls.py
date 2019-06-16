from django.urls import path
from .views import ChangePasswordView, ChangeLocationView, ChangeBankAccountView, ChangePhoneView
from .views import current_user, UserList, DatasetUploadView

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('change_password', ChangePasswordView.as_view()),
    path('change_location', ChangeLocationView.as_view()),
    path('change_account_number', ChangeBankAccountView.as_view()),
    path('change_phone', ChangePhoneView.as_view()),
    path('data_upload', DatasetUploadView.as_view())
]
