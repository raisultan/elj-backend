# Generated by Django 2.2.7 on 2019-11-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191116_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='lessons',
            field=models.ManyToManyField(to='core.Lesson'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='class_name',
            field=models.CharField(max_length=12),
        ),
    ]