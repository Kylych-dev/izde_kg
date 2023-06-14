# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# # from .managers import UserManager
# # from ..service import choices


# class UserModel(AbstractBaseUser):
#
#     email = models.EmailField(max_length=250, unique=True)
#     password = models.CharField(max_length=120, null=True)
#     first_name = models.CharField(max_length=250, null=True, blank=True)
#     last_name = models.CharField(max_length=255, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     gender = models.SmallIntegerField(choices=choices.GENDER_CHOICES, null=True)
#
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['gender']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.email

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from app.service import choices


class Language(models.Model):
    title = models.CharField(_("language"), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    photo = models.ImageField(_("photo"), blank=True, null=True)
    full_name = models.CharField(_("full_name"), max_length=60)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.IntegerField(blank=True, null=True)
    is_agent = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    languages = models.ManyToManyField(Language)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
