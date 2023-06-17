from django.contrib import admin
from . import models



@admin.register(models.CustomUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_filter = ['email']

    # class Meta:
    #     model = models.UserModel


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']



