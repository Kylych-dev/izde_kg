from django.contrib import admin #загрузка админки
from .models import Property, Address, City, District, FeedBack, Advertisement #импорт моделек 

class FeedBackInline(admin.TabularInline):
    """
    Класс для отображения отызвово
    """
    model = FeedBack
    extra = 0

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'address']
    list_filter = ['new_property',]
    inlines = [FeedBackInline]
    
    class Meta:
        model = Property





@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'additional_info']
    search_fields = ['price', 'deal_choices']

    class Meta:
        models = Advertisement
        
@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'comment', 'date']
    search_fields = ['user__username', 'property__storey', 'property__bedroom', 'property__bathroom']

admin.site.register(Address)
admin.site.register(City)
admin.site.register(District)

