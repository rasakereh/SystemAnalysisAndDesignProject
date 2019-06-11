from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from core.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, allow_blank=False)
    email = serializers.EmailField(allow_blank=False)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        Group.objects.get(name='workers').user_set.add(instance)
        Profile(user=instance).save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'email',)


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ChangeLocation(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('country', 'city')


class ChangeBankAccount(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('bank_account', )


class ChangePhone(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('phone', )

