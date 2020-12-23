from django.contrib import admin
from .models import Professor
# Register your models here.
class AdminProfessor(admin.ModelAdmin):
    list_display = ['name','email']
    
admin.site.register(Professor,AdminProfessor)
