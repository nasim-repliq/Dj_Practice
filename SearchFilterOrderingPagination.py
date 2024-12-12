# search Filter

from rest_framework.filters import SearchFilter

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['city']


# http://127.0.0.1:8000/studentapi/?search=Ranchi


# OrderingFilter

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    ordering_fields = ['name', 'city']
    ordering_fields = '__all__'
    
# ?ordering=name



# PAGINATION
#PageNumberPagination
class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'records'
    max_page_size = MyPageNumberPagination

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination

# CursorPagination
from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'
    cursor_query_param = 'cu'