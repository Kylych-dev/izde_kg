from django.contrib import admin
from . import models

'''
Image
Property
Advertisement
Address
City
District
FeedBack

'''


@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'address']
    list_filter = ['new_property',]

    class Meta:
        model = models.Property

@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'additional_info']
    search_fields = ['price', 'deal_choices']

    class Meta:
        models = models.Advertisement
