from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    birthday = models.DateField()
    
    def __str__(self) -> str:
        return self.name
    
class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'), 
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    
    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices= LEVEL, blank=False, null = False, default = 'B')
    
    def __str__(self) -> str:
        return self.description

class Registration(models.Model):
    SHIFT = (
        ('D', 'Day'), 
        ('S', 'Swing'),
        ('N', 'Night'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    shift = models.CharField(max_length=1, choices=SHIFT, blank=False, null=False, default = 'M')
    