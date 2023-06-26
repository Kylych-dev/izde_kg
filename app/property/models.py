from django.db import models
from django.utils.translation import gettext_lazy as _
from ..oauth.models import CustomUser
import random
import os
from django.urls import reverse
from ..service import choices, service

bm = dict(blank=True, max_length=300)


class Image(models.Model):
    property = models.ForeignKey(
        'Property', related_name='images', on_delete=models.CASCADE)
    file = models.ImageField(
        upload_to=service.upload_image_path, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.pk}'
    
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Property(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    storey = models.CharField(
        _('storey'), **bm, choices=choices.STOREY, unique=False)
    bedroom = models.CharField(
        _('bed'), max_length=300, choices=choices.BEDROOM, unique=True)
    bathroom = models.CharField(
        _('bathroom'), max_length=300, choices=choices.BATHROOM, unique=False)
    furnished = models.CharField(
        _('furnished'), **bm, choices=choices.FURNISHED, unique=False)
    parking_space = models.CharField(
        _('parking_space'), **bm, choices=choices.PARKING_SPACE, unique=False)
    new_property = models.CharField(
        _('new_property'), **bm, choices=choices.NEW_PROPERTY, unique=False)  # новая или не новая
    purpose = models.CharField(
        _('purpose'), **bm, choices=choices.PURPOSE, unique=True)  # цель назначение
    square_meter = models.DecimalField(
        blank=True, decimal_places=2, max_digits=20, default=0.00)
    address = models.ForeignKey('Address', verbose_name=_(
        "Address"), on_delete=models.CASCADE, blank=True)

    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимости'


class Advertisement(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='property_advertisement')
    deal_choices = models.CharField(
        _('deal'), max_length=10, choices=choices.DEAL)
    currency_choices = models.CharField(
        _('currency'), max_length=10, choices=choices.CURRENCY)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    additional_info = models.TextField()
    feedback = models.ManyToManyField('FeedBack', default=None, blank=True) #
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    duration = models.CharField(
        _('duration'), **bm, choices=choices.DURATION, unique=False)
    wishlist = models.ManyToManyField(CustomUser, related_name='wishlist_advertisement',
                                      default=None, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Address(models.Model):
    region = models.CharField(
        _('region'), **bm, choices=choices.REGION_CHOICES, unique=False)
    city = models.ForeignKey('City', verbose_name=_(
        "City"), on_delete=models.CASCADE, blank=True)
    district = models.ForeignKey('District', verbose_name=_(
        "District"), on_delete=models.CASCADE, blank=True)
    street = models.CharField(max_length=50, verbose_name='street')
    apartment = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.street) + str(self.apartment)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class City(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class District(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class FeedBack(models.Model):
    """_summary_
    Моделька отзывов 
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='feedback')
    comment = models.TextField()
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property} - {self.user} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
