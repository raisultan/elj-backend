from rest_framework import serializers

from core.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for lesson objects"""

    class Meta:
        model = Lesson
        fields = ('id', 'subject_name', 'number', 'cabinet', 'time',)
        read_only_fields = ('id', )
