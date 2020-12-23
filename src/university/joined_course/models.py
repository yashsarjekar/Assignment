from django.db import models
from students.models import Student
from courses.models import Course
# Create your models here.
class JoinedCourse(models.Model):
    student = models.ForeignKey(Student ,on_delete=models.CASCADE,default=1)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default=1)