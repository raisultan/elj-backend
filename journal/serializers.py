from rest_framework import serializers
from core.models import (
    StudyYear,
    Subject,
    Mark,
    StudentClass,
    Student,
    TeacherSubject,
    School,
)


class StudyYearSerializer(serializers.ModelSerializer):
    """Serializer for study year objects"""

    class Meta:
        model = StudyYear
        fields = ('id', 'year')
        read_only_fields = ('id',)


class SubjectSerializer(serializers.ModelSerializer):
    """Serializer for subject object"""

    class Meta:
        model = Subject
        fields = ('id', 'name')
        read_only_fields = ('id',)


class StudentClassSerializer(serializers.ModelSerializer):
    """Serializer for class object"""

    class Meta:
        model = StudentClass
        fields = ('id', 'name')
        read_only_fields = ('id',)


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for student object"""
    student_class = StudentClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'surname', 'name', 'lastname', 'birth_date',
                  'address', 'phone', 'student_class')
        read_only_fields = ('id',)


class MarkSerializer(serializers.ModelSerializer):
    """Serializer for mark object"""
    subject = SubjectSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), source='subject', write_only=True
    )
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True
    )

    class Meta:
        model = Mark
        fields = ('id', 'value', 'date', 'subject',
                  'student', 'subject_id', 'student_id')
        read_only_fields = ('id',)


class TeacherSubjectSerializer(serializers.ModelSerializer):
    """Serializer for subject object"""
    student_classes = StudentClassSerializer(read_only=True, many=True)

    class Meta:
        model = TeacherSubject
        fields = ('id', 'name', 'student_classes')
        read_only_fields = ('id',)


class SchoolSerializer(serializers.ModelSerializer):
    """Serializer for school object"""

    class Meta:
        model = School
        fields = ('id', 'name', 'address', 'phone')
        read_only_fields = ('id', )
