# Generated by Django 2.2 on 2020-12-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20201222_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='professor_id',
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
