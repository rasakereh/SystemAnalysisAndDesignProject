from profile_manager.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'phone_num', 'city', 'country', 'gender', 'avatar')
