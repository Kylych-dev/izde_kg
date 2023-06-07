from django.db import models

from django.utils.translation import gettext_lazy as _

import random 
import os
from django.urls import reverse
from ..service import choices
from ..service import service


bm = dict(blank=True, max_length=300)



class Property(models.Model):
    # realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    address = models.CharField(blank=True, max_length=300)
    description = models.TextField()
    # city
    # category = models.ForeignKey(Category, default='', max_length=300, unique=False, on_delete=models.CASCADE)
    storey = models.CharField(_('storey'), **bm, choices=choices.STOREY, unique=False)
    bedroom = models.CharField(_('bed'), max_length=300, choices=choices.BEDROOM, unique=True)
    bathroom = models.CharField(_('bathroom'), max_length=300, choices=choices.BATHROOM, unique=False)
    furnished = models.CharField(_('furnished'), **bm, choices=choices.FURNISHED, unique=False)
    parking_space = models.CharField(_('parking_space'), **bm, choices=choices.PARKING_SPACE, unique=False)
    new_property = models.CharField(_('new_property'), **bm, choices=choices.NEW_PROPERTY, unique=False)
    purpose = models.CharField(_('porpose'), **bm, choices=choices.PURPOSE, unique=True)
    duration = models.CharField(_('duration'), **bm, choices=choices.DURATION, unique=False)

    square_meter = models.DecimalField(blank=True, decimal_places=2, max_digits=20, default=0.00)
    price = models.DecimalField(decimal_places=0, max_digits=20, default=0.00)
    main_image = models.ImageField(upload_to=service.upload_image_path, null=True, blank=True)
    featrued = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug
    
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Property'



class PropertyRating(models.Model):
    # user = models.ForeignKey(User)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    verfied = models.BooleanField(default=False)

    def __str__(self):
        return self.property.count