from django.contrib import admin
from django.urls import path
from .views import ProfessorLogin
urlpatterns = [
    path('', ProfessorLogin.as_view()),
]