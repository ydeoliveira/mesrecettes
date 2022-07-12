from django.urls import path
from menu.views import Courses

urlpatterns = [
        path('courses/<int:pk>/', Courses.as_view(), name='courses'),

]