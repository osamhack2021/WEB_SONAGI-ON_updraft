from django.contrib import admin
from .models import Diary

# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'title', 'content', 'emotion', 'write_date', 'rewrite_date') 

admin.site.register(Diary, DiaryAdmin)