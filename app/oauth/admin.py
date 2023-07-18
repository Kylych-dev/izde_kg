from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'full_name']
    fieldsets = ((None, {'fields': ('email', 'password')
                         }
                  ),
                 (_('Personal info'), {'fields':
                       ('full_name', 'photo', 'phone')
                                       }
                  ),
                 (_('Permissions'),
                  {'fields':
                       ('is_active', 'is_staff', 'is_agent', 'is_superuser')
                   }
                  ),
                 (_('Additional info'),
                  {'fields': ('region', 'languages', 'description')
                   }
                  ),

                 (_('Important dates'),
                  {'fields': ('last_login', 'date_joined')
                   }
                  )

                 )
    readonly_fields = ['last_login', 'date_joined']
    add_fieldsets = ((None, {'classes': ('wide',),
                             'fields': ('email',
                                        'password1',
                                        'password2')}),)


admin.site.register(models.CustomUser, UserAdmin)


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


# @admin.register(models.CustomUser)
# class UserModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'full_name']
#     list_filter = ['email']
#     #
#     inlines = [FeedBackInline, ]
#     # class Meta:
#     #     model = models.UserModel


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


admin.site.register(models.Feedback)
admin.site.register(models.Region)
