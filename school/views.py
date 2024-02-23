from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer  import StudentSerializer, CourseSerializer, RegistrationSerializer, RegistrationStudentListSerializer, StudentRegistrationListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(viewsets.ModelViewSet):
    """
    Showing all students
    """
    queryset = Student.objects.all();
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CoursesViewSet(viewsets.ModelViewSet):
    """
    Showing all courses
    """
    queryset = Course.objects.all();
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationsViewSet(viewsets.ModelViewSet):
    """
    Showing all courses
    """
    queryset = Registration.objects.all();
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationStudentList(generics.ListAPIView):
    """
    Listing all registrations of a student
    """
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk']);
        return queryset
    
    serializer_class = RegistrationStudentListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentRegistrationList(generics.ListAPIView):
    """
    Listing all registrations of a student
    """
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk']);
        return queryset
    
    serializer_class = StudentRegistrationListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    