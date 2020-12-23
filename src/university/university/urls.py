"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from students.views import Login,logout
from courses.views import show_student_course
from professors.views import professor_logout,create_course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('courses.urls')),
    path('register',include('students.urls')),
    path('login',Login.as_view()),
    path('logout',logout),
    path('view_course',show_student_course),
    path('create_courese',create_course),
    path('professor_logout',professor_logout),
    path('professor_login',include('professors.urls')),
    path('professor_dashboard',include('professors.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
