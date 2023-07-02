from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from .managers import UserManager
from ..service import choices

# from phonenumber_field.modelfields import PhoneNumberField


class Language(models.Model):
    title = models.CharField(_("language"), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"


class Region(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    photo = models.ImageField(_("photo"), blank=True, null=True)
    full_name = models.CharField(_("full_name"), max_length=60)
    email = models.EmailField(_("email address"), unique=True)

    phone = models.IntegerField(_('phone'), blank=True, null=True)
    description = models.TextField(_('description'), blank=True, null=True)
    is_agent = models.BooleanField(_('is_agent'), default=False)
    date_joined = models.DateTimeField(_('date_joined'), auto_now_add=True)

    languages = models.ManyToManyField(Language)
    experience = models.IntegerField(_('experience'), blank=True, null=True)
    region = models.ManyToManyField(Region)

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

    # def clean(self):
    #     if not self.author.is_agent:
    #         raise ValidationError("Only agents can receive feedback.")


class Feedback(models.Model):
    agent = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="feedbacks_received")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='feedbacks_given')
    comment = models.TextField(_("comment"))

    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    date = models.DateTimeField(_('date'), auto_now_add=True)

    def __str__(self):
        return f" {self.agent} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


