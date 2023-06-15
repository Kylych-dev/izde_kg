from django.contrib import admin
from . import models
from app.realtor.models import Agent


@admin.register(models.CustomUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_filter = ['email']

    # class Meta:
    #     model = models.UserModel


admin.site.register(Agent)
