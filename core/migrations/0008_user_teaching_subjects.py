# Generated by Django 2.2.7 on 2019-11-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_teachersubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teaching_subjects',
            field=models.ManyToManyField(blank=True, to='core.TeacherSubject'),
        ),
    ]
