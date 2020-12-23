# Generated by Django 2.2 on 2020-12-22 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0003_remove_student_course'),
        ('courses', '0008_auto_20201222_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]
