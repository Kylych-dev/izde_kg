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

    # main = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}'


class Property(models.Model):
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
        _('new_property'), **bm, choices=choices.NEW_PROPERTY, unique=False)
    purpose = models.CharField(
        _('porpose'), **bm, choices=choices.PURPOSE, unique=True)
    duration = models.CharField(
        _('duration'), **bm, choices=choices.DURATION, unique=False)
    square_meter = models.DecimalField(
        blank=True, decimal_places=2, max_digits=20, default=0.00)
    # images = models.ManyToManyField(Image, related_name='prop_images')
    featrued = models.BooleanField(default=False)
    address = models.ForeignKey('Address', verbose_name=_(
        "Address"), on_delete=models.CASCADE, blank=True)
    slug = models.SlugField(max_length=100)

    # price = models.DecimalField(decimal_places=0, max_digits=20, default=0.00)
    # main_image = models.OneToOneField(Image, related_name='property')
    # description = models.TextField()
    # slug = models.SlugField(blank=True, unique=True)
    # title = models.CharField(max_length=120)
    # realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, default='', max_length=300, unique=False, on_delete=models.CASCADE)
    # images = models.ImageField(upload_to=service.upload_image_path, null=True, blank=True)
    # active = models.BooleanField(default=True)
    # timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property'


class Advertisement(models.Model):
    deal_choices = models.CharField(
        _('deal'), max_length=10, choices=choices.DEAL)
    currency_choices = models.CharField(
        _('currency'), max_length=10, choices=choices.CURRENCY)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateField()
    additional_info = models.TextField()
    feedback = models.ManyToManyField('FeedBack')


class Address(models.Model):
    region = models.CharField(
        _('region'), **bm, choices=choices.REGION_CHOICES, unique=False)

    city = models.ForeignKey('City', verbose_name=_(
        "City"), on_delete=models.CASCADE, blank=True)
    district = models.ForeignKey('District', verbose_name=_(
        "District"), on_delete=models.CASCADE, blank=True)

    street = models.CharField(max_length=50, verbose_name='street')
    apartment = models.PositiveSmallIntegerField()


class City(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='property_id')
    comment = models.TextField()
    date = models.DateTimeField()

    def __str__(self) -> str:
        return self.property, self.property, self.date


'''
class PropertyRating(models.Model):
    user = models.ForeignKey(UserModel)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    verfied = models.BooleanField(default=False)

    def __str__(self):
        return self.property.count
'''
