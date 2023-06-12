from django.contrib import admin
from . import models

@admin.register(models.UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name']
    list_filter = ['email']

    # class Meta:
    #     model = models.UserModel