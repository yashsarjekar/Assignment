from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from .models import Student
# Create your views here.
class Register(View):

    def get(self, request):
        return render(request,'register.html',{})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            err = "Password Does not Match"
            return render(request, 'register.html',{'err':err})
        else:
            email_err = Student.check_user_exist(email)
            if email_err == True:
                hash_password = make_password(password)
                new_cust = Student(email=email,password=hash_password)
                new_cust.save()
                success_msg = "Successfully Created Student Account"
                return render(request, 'register.html',{'success_msg':success_msg})

            else:
                return render(request, 'register.html',{'err':email_err})

class Login(View):
    def get(self, request):
        return render(request, 'login.html',{})

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            student = Student.objects.get(email=email)
            msg = ""
            if student:
                result = check_password(password,student.password)
                if result == True:
                    msg = "Authentication Successful"
                    request.session['student_id'] = student.id
                    request.session['student_email'] = student.email
                    return redirect('home_page')
                else:
                    msg = "Password Incorrect"
                    return render(request,'login.html',{'err':msg})
            else:
                msg = "User is Not Registered"
                return render(request,'login.html',{'err':msg})
        except Student.DoesNotExist:
            msg = "User is Not Registered"
            return render(request,'login.html',{'err':msg})


def logout(request):
    request.session.clear()
    return redirect('home_page')

    