from django.shortcuts import render,redirect
from django.views import View
from .models import Course
from joined_course.models import JoinedCourse
from students.models import Student
# Create your views here.
class Index(View):
    def get(self,request):
        

        courses = Course.get_courses()
        return render(request, 'index.html',{'courses': courses})
    
    def post(self,request):
        course_id = request.POST.get('course_id')
        print(course_id)
        student_id = request.session.get('student_id')
        student_inst = Student.objects.get(id = student_id)
        course_inst = Course.objects.get(id = course_id)
        try:
            stud = JoinedCourse.objects.get(student  = student_inst)
            if stud:
                print("You Cannot Enroll more than one Course")
                return redirect('home_page')
            else:
                rela = JoinedCourse(student = student_inst,course = course_inst)
                rela.save()
        except JoinedCourse.DoesNotExist:
            rela = JoinedCourse(student = student_inst,course = course_inst)
            rela.save()      
            return redirect('home_page')

def show_student_course(request):
    if request.method == 'GET':
        student_id = request.session.get('student_id')
        student_inst = Student.objects.get(id = student_id)
        try:
            rel = JoinedCourse(student = student_inst)
            if rel:
                course = rel.course
                return render(request,'view_course.html',{'course':course})
            else:
                return render(request,'view_course.html',{})
        except JoinedCourse.DoesNotExist:
            return render(request,'view_course.html',{})

