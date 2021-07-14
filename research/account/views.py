from rest_framework import viewsets
from models import User, Profile
from views import UserSerializer, ProfileRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    custom user viewset
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    profile viewset
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer