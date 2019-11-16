from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Event
from event import serializers


class EventViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    """Manage events in the database"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer

    def get_queryset(self):
        """Return events for the current authenticated user only"""
        return self.queryset.filter(teacher=self.request.user).order_by('id')

    def perform_create(self, serializer):
        """Create a new event"""
        return serializer.save(teacher=self.request.user)
