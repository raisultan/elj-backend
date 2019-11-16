from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Lesson, Day

from timetable import serializers


class LessonViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,):
    """Manage lessons in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

    def get_queryset(self):
        """Return lessons for current authenticated user"""
        return self.queryset.filter(
            teacher=self.request.user).order_by('number')

    def perform_create(self, serializer):
        """Create a new lesson"""
        return serializer.save(teacher=self.request.user)


class DayViewSet(viewsets.ModelViewSet):
    """Manage days in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Day.objects.all()
    serializer_class = serializers.DaySerializer

    def get_queryset(self):
        """Return days for current authenticated user"""
        return self.queryset.filter(
            teacher=self.request.user).order_by('id')

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.DayDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new day"""
        return serializer.save(teacher=self.request.user)
