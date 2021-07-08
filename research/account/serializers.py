from rest_framework import serializers
from account.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    """
    유저
    """
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'last_name',
            'first_name'
        )


class ProfileRegisterSerializer(serializers.ModelSerializer):
    """
    프로필 생성
    """

    class Meta:
        model = Profile
        fields = (
            'nickname',
            'status',
        )


class ProfileSerializer(serializers.ModelSerializer):
    """
    프로필
    """

    class Meta:
        model = Profile
        fields = (
            'nickname',
            'status',
        )

    @staticmethod
    def get_is_profile_completed(instance):
        return instance.status != Profile.Status.ON_SIGNUP
