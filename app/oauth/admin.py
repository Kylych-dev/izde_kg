from django.contrib import admin
from . import models
from app.realtor.models import Agent
from app.realtor.models import Language


@admin.register(models.CustomUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_filter = ['email']

    # class Meta:
    #     model = models.UserModel


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']




admin.site.register(Agent)
admin.site.register(Language)
