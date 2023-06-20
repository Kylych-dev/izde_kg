from django.contrib import admin
from . import models


class FeedBackInline(admin.TabularInline):
    """
    Класс для отображения отзывов для агентов
    """
    model = models.Feedback
    extra = 0
    fk_name = 'agent'

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj and not obj.is_agent:
            formset.extra = 0
        return formset


@admin.register(models.CustomUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_filter = ['email']

    inlines = [FeedBackInline, ]
    # class Meta:
    #     model = models.UserModel


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


admin.site.register(models.Feedback)
admin.site.register(models.Region)
