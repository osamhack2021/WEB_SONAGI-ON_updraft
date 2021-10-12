from django.contrib import admin
from .models import UserSetting

# Register your models here.

class UserSettingAdmin(admin.ModelAdmin):
    list_display = ('email', 
                    'nickname', 
                    'major', 
                    'type', 
                    'enlisted_date', 
                    'delisted_date', 
                    'promotion1_date',
                    'promotion2_date',
                    'promotion3_date') 

    def has_delete_permission(self, request, obj=None):
        #Disable delete
        return False

admin.site.register(UserSetting, UserSettingAdmin)