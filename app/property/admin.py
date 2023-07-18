from django.contrib import admin  # загрузка админки
# импорт моделек
from .models import Property, Address, City, District, FeedBack, Advertisement, Image


class FeedBackInline(admin.TabularInline):
    """
    Класс для отображения отызвово
    """
    model = FeedBack
    extra = 0


class PropertyImagesInline(admin.TabularInline):
    model = Image
    extra = 5  # Максимальное количество фотографий


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'address']
    list_filter = ['new_property',]
    inlines = [PropertyImagesInline, FeedBackInline]

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
    search_fields = ['user__username', 'property__storey',
                     'property__bedroom', 'property__bathroom']


admin.site.register(Address)
admin.site.register(City)
admin.site.register(District)
