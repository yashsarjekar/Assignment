from django.contrib import admin
from .models import JoinedCourse
# Register your models here.

class JoinedCourseAdmin(admin.ModelAdmin):
    list_display = ['student','course']

admin.site.register(JoinedCourse,JoinedCourseAdmin)
