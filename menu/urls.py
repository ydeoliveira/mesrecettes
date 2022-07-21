from django.urls import path
from menu.views import Courses, MenuList

urlpatterns = [
        path('all/', MenuList.as_view(), name='menus'),
        path('courses/<int:pk>/', Courses.as_view(), name='courses'),

]