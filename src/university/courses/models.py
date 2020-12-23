from django.db import models
from professors.models import Professor
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    professor_id = models.ForeignKey(Professor ,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default="Hey its Cool")
    images =  models.ImageField(upload_to="course_images/")
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    @staticmethod
    def get_courses():
        return Course.objects.all()

    @staticmethod
    def get_courses_by_professor(professor_id):
        print(professor_id)
        if professor_id is not None:
            return Course.objects.filter(professor_id= professor_id)
        else:
            Course.get_courses()
