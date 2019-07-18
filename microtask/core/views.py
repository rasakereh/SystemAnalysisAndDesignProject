import threading
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Profile, ImageLabelingTask
from .serializers import UserSerializer, UserSerializerWithToken, ChangePasswordSerializer, ChangeLocation, \
    ChangeBankAccount, ChangePhone, DocumentSerializer, ImageSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerWithToken
from .models import Document, Dataset
from .upload import chopToMicrotasks, saveFile, validateUpload
import zipfile
import os
from django.conf import settings
from core.models import Image
from rest_framework import viewsets


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeLocationView(UpdateAPIView):
    model = Profile
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeLocation

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangeLocation(data=request.data)

        if serializer.is_valid():
            p = Profile.objects.get(user=self.object)
            p.city = serializer.data.get('city')
            p.country = serializer.data.get('country')
            p.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeBankAccountView(UpdateAPIView):
    model = Profile
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeBankAccount

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangeBankAccount(data=request.data)

        if serializer.is_valid():
            p = Profile.objects.get(user=self.object)
            p.bank_account = serializer.data.get('bank_account')
            p.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePhoneView(UpdateAPIView):
    model = Profile
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePhone

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePhone(data=request.data)

        if serializer.is_valid():
            p = Profile.objects.get(user=self.object)
            p.phone = serializer.data.get('phone')
            p.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DatasetUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        new_doc = DocumentSerializer(data=request.data)
        if new_doc.is_valid():
            new_doc.save()
            dataset = Dataset(document=Document.objects.latest('id'))
            dataset.dataType = request.data['dataType']
            dataset.save()
            if request.data['dataType'] == 'Image Labeling':
                zip_ref = zipfile.ZipFile(os.path.join(settings.MEDIA_ROOT, Document.objects.latest('id').doc_file.name), 'r')
                zip_ref.extractall(os.path.join(settings.MEDIA_ROOT))
                zip_ref.close()
                print('extract successfull')
                dirs = os.listdir(path=os.path.join(settings.MEDIA_ROOT))
                print(dirs)
                for dir in dirs:
                    if dir == 'documents' or dir == 'images':
                        continue
                    for r, d, f in os.walk(top=os.path.join(settings.MEDIA_ROOT)):
                        for file in f:
                            img = Image(name=file)
                            img.image = os.path.join(dir, file)
                            img.save()
                            img_task = ImageLabelingTask(content=Image.objects.latest('id'), category=dir)
                            img_task.save()
                            

            elif request.data['dataType'] == 'Voice To Text':
                pass
            elif request.data['dataType'] == 'Text To Voice':
                pass
            elif request.data['dataType'] == 'Text To Text':
                pass

            return Response(status=204)

        return Response(new_doc.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer