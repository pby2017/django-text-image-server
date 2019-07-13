from django.contrib import admin
from diary.models import Diary
from diary.models import Image

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'description', 'image')
    list_filter = ('date_time',)
    search_fields = ('requesterID', 'date_time', 'patient_id')

admin.site.register(Diary, DiaryAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    list_filter = ('id',)
    search_fields = ('id', 'image')

admin.site.register(Image, ImageAdmin)