# Generated by Django 2.2 on 2020-12-21 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_professor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='professor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='professors.Professor'),
        ),
    ]
