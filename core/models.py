from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Email address is required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Event(models.Model):
    """Event object to be used in app"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Lesson to be used in timetable"""
    subject_name = models.CharField(max_length=255)
    number = models.IntegerField()
    cabinet = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    class_name = models.CharField(max_length=12)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.subject_name


class Day(models.Model):
    """Day to be used in timetable"""
    DAYS_OF_THE_WEEK = (
        ('MON', _('Понедельник')),
        ('TUE', _('Вторник')),
        ('WED', _('Среда')),
        ('THU', _('Четверг')),
        ('FRI', _('Пятница')),
        ('SAT', _('Суббота')),
    )
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_THE_WEEK)
    lessons = models.ManyToManyField('Lesson')
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.day_of_week
