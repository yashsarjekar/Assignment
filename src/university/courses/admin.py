from django.contrib import admin
from .models import Course
# Register your models here.

class AdminCourse(admin.ModelAdmin):
    list_display = ['title','professor_id']


admin.site.register(Course,AdminCourse)
