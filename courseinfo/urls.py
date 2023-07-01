"""rutherford_john_ezu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from courseinfo.views import (
    SectionList,
    CourseList,
    SemesterList,
    StudentList,
    RegistrationList,
    InstructorList,
    InstructorDetail,
    SectionDetail,
    SemesterDetail,
    CourseDetail,
    StudentDetail,
    RegistrationDetail,
    InstructorCreate,
    SectionCreate,
    CourseCreate,
    SemesterCreate,
    StudentCreate,
    RegistrationCreate,

)



urlpatterns = [
    path('instructor/',
         InstructorList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),

    path('instructor/<int:pk>/',
        InstructorDetail.as_view(),
        name='courseinfo_instructor_detail_urlpattern'),

    path('instructor/create/',
         InstructorCreate.as_view(),
            name='courseinfo_instructor_create_urlpattern'),

    path('section/',
         SectionList.as_view(),
         name='courseinfo_section_list_urlpattern'),

    path('section/<int:pk>/',
        SectionDetail.as_view(),
        name='courseinfo_section_detail_urlpattern'),

    path('section/Create/',
         SectionCreate.as_view(),
         name='courseinfo_section_create_urlpattern'),

    path('course/',
         CourseList.as_view(),
         name='courseinfo_course_list_urlpattern'),

    path('course/<int:pk>/',
         CourseDetail.as_view(),
         name='courseinfo_course_detail_urlpattern'),

    path('course/Create/',
         CourseCreate.as_view(),
         name='courseinfo_course_create_urlpattern'),

    path('semester/',
         SemesterList.as_view(),
         name='courseinfo_semester_list_urlpattern'),

    path('semester/<int:pk>/',
        SemesterDetail.as_view(),
        name='courseinfo_semester_detail_urlpattern'),

    path('semester/Create/',
         SemesterCreate.as_view(),
         name='courseinfo_semester_create_urlpattern'),

    path('student/',
         StudentList.as_view(),
         name='courseinfo_student_list_urlpattern'),

    path('student/<int:pk>/',
         StudentDetail.as_view(),
         name='courseinfo_student_detail_urlpattern'),

    path('student/Create/',
         StudentCreate.as_view(),
         name='courseinfo_student_create_urlpattern'),

    path('registration/',
         RegistrationList.as_view(),
         name='courseinfo_registration_list_urlpattern'),

    path('registration/<int:pk>/',
         RegistrationDetail.as_view(),
         name='courseinfo_registration_detail_urlpattern'),

    path('registration/Create/',
         RegistrationCreate.as_view(),
         name='courseinfo_registration_create_urlpattern'),

]

