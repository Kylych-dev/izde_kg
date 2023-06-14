from django.contrib import admin
from . import models
from .models import Property, Address, City, District, FeedBack

'''
Image
Property
Advertisement
Address
City
District
FeedBack

'''
class FeedBackInline(admin.TabularInline):
    model = FeedBack
    extra = 0

@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'address']
    list_filter = ['new_property',]
    inlines = [FeedBackInline]
    
    class Meta:
        model = models.Property





@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'additional_info']
    search_fields = ['price', 'deal_choices']

    class Meta:
        models = models.Advertisement
        
@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'comment', 'date']
    search_fields = ['user__username', 'property__storey', 'property__bedroom', 'property__bathroom']

admin.site.register(Address)
admin.site.register(City)
admin.site.register(District)

