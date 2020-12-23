from django.shortcuts import render,redirect
from django.views import View
from .models import Professor
from courses.models import Course
from courses.form import CourseForm
from .models import Professor
from django.http import HttpResponse
# Create your views here.
class ProfessorLogin(View):
    def get(self, request):
        prof = request.session.get('professor_id')
        if prof:
            courses = Course.get_courses_by_professor(prof)
            render(request,'professor_dashboard.html',{'courses':courses})
        return render(request, 'professor_login.html',{})
    def post(self, request):
        request.session['professor_id'] = None
        prof = request.session.get('professor_id')
        if prof:
            courses = Course.get_courses_by_professor(prof)
            render(request,'professor_dashboard.html',{'courses':courses})
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            professor = Professor.objects.get(email=email)
            msg = ""
            if professor:
                if password == professor.password:
                    msg = "Authentication Successful"
                    request.session['professor_id'] = professor.id
                    request.session['professor_email'] = professor.email
                    request.session['professor_name'] = professor.name
                    prof = request.session.get('professor_id')
                    if prof:
                        courses = Course.get_courses_by_professor(prof)
                        return render(request,'professor_dashboard.html',{'courses':courses})
                else:
                    msg = "Password Incorrect"
                    return redirect('professor_dashboard.html',{})
            else:
                msg = "User is Not Registered"
                return render(request,'professor_login.html',{'err':msg})
        except Professor.DoesNotExist:
            msg = "User is Not Registered"
            return render(request,'professor_login.html',{'err':msg})
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            form = CourseForm()
            return render(request, 'professor_dashboard.html', {'form': form})
def professor_logout(request):
    request.session.clear()
    return redirect('home_page')