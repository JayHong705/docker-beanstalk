from rest_framework import authentication
from research.account import Profile


class AuthenticationV2(authentication.BaseAuthentication)
    def authenticate(self, request):
        try:
            profile = request.user.profile
            if profile.status == Profile.NOT_SIGNUP or profile.status == Profile.WITHDRAWAL or profile.status == Profile.SUSPENDED:
                return None
            return user
        except:
            return None
