from django.contrib import admin
from school.models import Student, Course

class Students(admin.ModelAdmin):
    # Data that may be visible
    list_display = ('id', 'name', 'rg', 'cpf', 'birthday',)
    
    # Data that may be updated
    list_display_links = ('id', 'name')
    
    search_fields = ('id', 'name', 'rg', 'cpf')
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description', 'level')
    list_display_links = ('id', 'course_code', 'description')
    search_fields = ('id', 'course_code', 'level')
    

admin.site.register(Course, Courses)