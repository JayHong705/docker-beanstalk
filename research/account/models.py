from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """
    User Model
    """
    email = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=31, blank=True, help_text='성')
    first_name = models.CharField(max_length=31, blank=True, help_text='이름')
    phone_number = models.CharField(max_length=12, blank=True, help_text='핸드폰 번호')

    USERNAME_FIELD = 'email'

class Profile(models.Model):
    """
    유저 프로필
    """
    class Status(models.TextChoices):
        ON_SIGNUP = 'ON_SIGNUP', _('가입 중')
        PROFILE_CREATED = 'PROFILE_CREATED', _('프로필 생성 완료')
        IDENTITY_AUTHENTICATED = 'IDENTITY_AUTHENTICATED', _('본인인증 완료')
        WITHDRAWAL = 'WITHDRAWAL', _('탈퇴')
        SUSPENDED = 'SUSPENDED', _('이용 정지')

    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='유저')
    nickname = models.CharField(max_length=32, blank=True)
    status = models.CharField(
        max_length=31,
        choices=Status.choices,
        default=Status.ON_SIGNUP,
        help_text='유저 가입 상태'
    )
