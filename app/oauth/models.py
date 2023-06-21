from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class Language(models.Model):
    title = models.CharField(_("language"), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"


class Region(models.Model):
    title = models.CharField(max_length=20)


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


class FeedBack(models.Model):
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="feedback_agent")
    author = models.ForeignKey(
                               CustomUser, on_delete=models.CASCADE, related_name='author_feedback')
    comment = models.TextField(_('comment'))
    parent_comment = models.ForeignKey(
                                       'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    date = models.DateTimeField(_('date'), auto_now_add=True)

    def __str__(self):
        return f" {self.agent} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
