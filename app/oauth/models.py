from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from ..service import choices



class UserModel(AbstractBaseUser):

    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=120, null=True)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.SmallIntegerField(choices=choices.GENDER_CHOICES, null=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']

    objects = UserManager()

    def __str__(self):
        return self.email