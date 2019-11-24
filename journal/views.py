from itertools import chain

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    StudyYear,
    Subject,
    Mark,
    StudentClass,
    Student,
    School,
)
from journal import serializers


class BaseJournalAttrViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,):
    """Base viewset for journal attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class StudyYearViewSet(BaseJournalAttrViewSet):
    """Manage study year in the database"""
    queryset = StudyYear.objects.all()
    serializer_class = serializers.StudyYearSerializer


class SubjectViewSet(BaseJournalAttrViewSet):
    """Manage subjects in the database"""
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class MarkViewSet(BaseJournalAttrViewSet,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin):
    """Manage marks in the database"""
    queryset = Mark.objects.all()
    serializer_class = serializers.MarkSerializer

    def get_queryset(self):
        """Retrieve all marks by student and subject"""
        queryset = self.queryset
        student = self.request.query_params.get('student')
        subject = self.request.query_params.get('subject')
        if student:
            queryset = queryset.filter(student__id=student)
        if subject:
            queryset = queryset.filter(subject__id=subject)

        return queryset


class StudentClassViewSet(BaseJournalAttrViewSet):
    """Manage classes in the database"""
    queryset = StudentClass.objects.all()
    serializer_class = serializers.StudentClassSerializer


class StudentViewSet(BaseJournalAttrViewSet):
    """Manage students in the database"""
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        """Retrieve students for authenticated user by class"""
        student_class = self.request.query_params.get('student_class', None)
        queryset = self.queryset
        if student_class:
            queryset = queryset.filter(student_class__name=student_class)

        return queryset


class JournalAPIView(viewsets.ModelViewSet):
    """Combine data from other serializer to form journal"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.MarkSerializer
    queryset = Mark.objects.all()

    def get_queryset(self):
        """Retrieve journal data from multiple serializers"""
        student_class = self.request.query_params.get('student_class', None)
        subject = self.request.query_params.get('subject', None)

        students_queryset = Student.objects.filter(
            student_class__name=student_class)
        mark_querysets = []

        for student in students_queryset:
            mark_querysets.append(student.marks.filter(subject__name=subject))

        queryset = list(chain(*mark_querysets))

        return queryset


class SchoolViewSet(BaseJournalAttrViewSet):
    """Manage school in the database"""
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer
