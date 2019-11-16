from rest_framework import serializers

from core.models import Lesson, Day


class LessonSerializer(serializers.ModelSerializer):
    """Serializer for lesson objects"""

    class Meta:
        model = Lesson
        fields = ('id', 'subject_name', 'number',
                  'cabinet', 'time', 'class_name')
        read_only_fields = ('id', )


class DaySerializer(serializers.ModelSerializer):
    """Serializer for the day object"""
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ('id', 'day_of_week', 'lessons')
        read_only_fields = ('id',)


class DayDetailSerializer(DaySerializer):
    """Serializer for a day detail"""
    lessons = LessonSerializer(many=True, read_only=True)
