from rest_framework import serializers

from core.models import Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer for event objects"""

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date')
        read_only_fields = ('id', )
