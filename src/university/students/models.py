from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=500)
    
    def __str__(self):
        return self.email
    
    @staticmethod
    def check_user_exist(email):
        try:
            em = Student.objects.filter(email=email)
            #print(len(em))
            if len(em) == 0:
                return True
            else:
                return "Student already Exist"
        except Student.DoesNotExist:
            return "Student already Exist"