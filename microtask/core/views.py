from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Profile
from .serializers import UserSerializer, UserSerializerWithToken, ChangePasswordSerializer, ChangeLocation, \
    ChangeBankAccount, ChangePhone
from django.contrib.auth.models import User


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
