from django.contrib import admin

from core import models


admin.site.register(models.User)
admin.site.register(models.Event)
admin.site.register(models.Lesson)
admin.site.register(models.Day)
admin.site.register(models.StudyYear)
admin.site.register(models.Subject)
admin.site.register(models.Mark)
admin.site.register(models.StudentClass)
admin.site.register(models.Student)
admin.site.register(models.TeacherSubject)
admin.site.register(models.School)
