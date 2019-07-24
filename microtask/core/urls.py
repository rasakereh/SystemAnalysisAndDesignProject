from django.urls import path
from .views import ChangePasswordView, ChangeLocationView, ChangeBankAccountView, ChangePhoneView
from .views import current_user, UserList, DatasetUploadView, ImageViewSet, VoiceViewSet, FetchTask, JobSubmitView

from django.conf.urls.static import static
from django.conf import settings


img_detail = ImageViewSet.as_view({
    'get': 'retrieve'
})
vc_detail = VoiceViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('change_password', ChangePasswordView.as_view()),
    path('change_location', ChangeLocationView.as_view()),
    path('change_account_number', ChangeBankAccountView.as_view()),
    path('change_phone', ChangePhoneView.as_view()),
    path('data_upload', DatasetUploadView.as_view()), 
    path('fetch_task', FetchTask.as_view()),
    path('submit_task', JobSubmitView.as_view()),
    path('contents/images/<int:pk>/', img_detail, name='img-detail'),
    path('contents/voices/<int:pk>/', vc_detail, name='vc-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
