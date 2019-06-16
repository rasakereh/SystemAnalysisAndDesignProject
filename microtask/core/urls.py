from django.urls import path
from .views import current_user, UserList, datasetUpload

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('current_user/uploadDataset', datasetUpload, name='uploadDataset')
]
