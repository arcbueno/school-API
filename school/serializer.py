from rest_framework import serializers
from school.models import Student, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields = ['id', 'name', 'rg', 'cpf', 'birthday']
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class RegistrationStudentListSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    shift = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['course', 'shift']
        
    def get_shift(self, obj):
        return obj.get_shift_display()
    

class StudentRegistrationListSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ['student_name',]
    

        
        