from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import diary.api

app_name='diary'

router = routers.DefaultRouter()
router.register('diary', diary.api.DiaryViewSet)
router.register('image', diary.api.ImageViewSet)

urlpatterns = [
    path('restful/doc/', get_swagger_view(title='Rest API Document')),
    path('restful/', include((router.urls, 'diary'), namespace='api')),
]