from django.urls import path, include
from rest_framework.routers import DefaultRouter

from timetable import views


router = DefaultRouter()
router.register('lessons', views.LessonViewSet)
router.register('days', views.DayViewSet)

app_name = 'timetable'

urlpatterns = [
    path('', include(router.urls)),
]
