from django.urls import path
from menu.views import Courses, MenuList, GridMenu

urlpatterns = [
        path('all/', MenuList.as_view(), name='menus'),
        path('courses/<int:pk>/', Courses.as_view(), name='courses'),
        path('gridmenu/<int:pk>/', GridMenu.as_view(), name='gridmenu'),

]