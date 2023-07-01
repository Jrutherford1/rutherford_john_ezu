from django.shortcuts import render, get_object_or_404
from django.views import View

from courseinfo.forms import InstructorForm, SectionForm, CourseForm, SemesterForm, StudentForm, RegistrationForm
from courseinfo.models import Instructor
from courseinfo.models import Section
from courseinfo.models import Course
from courseinfo.models import Semester
from courseinfo.models import Student
from courseinfo.models import Registration
from courseinfo.utils import ObjectCreateMixin


class InstructorList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/instructor_list.html',
            {'instructor_list': Instructor.objects.all()}
        )


class InstructorDetail(View):
    def get(self, request, pk):
        instructor = get_object_or_404(Instructor, pk=pk)
        section_list = instructor.sections.all()
        return render(
            request,
            'courseinfo/instructor_detail.html',
            {'instructor': instructor,
             'section_list': section_list}
        )


class InstructorCreate(ObjectCreateMixin, View):
    form_class = InstructorForm
    template_name = 'courseinfo/instructor_form.html'


class SectionList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/section_list.html',
            {'section_list': Section.objects.all()}
        )


class SectionDetail(View):
    def get(self, request, pk):
        section = get_object_or_404(Section, pk=pk)
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()
        return render(
            request,
            'courseinfo/section_detail.html',
            {'section': section,
             'semester': semester,
             'course': course,
             'instructor': instructor,
             'registration_list': registration_list
            }
        )


class SectionCreate(ObjectCreateMixin, View):
    form_class = SectionForm
    template_name = 'courseinfo/section_form.html'



class CourseList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/course_list.html',
            {'course_list': Course.objects.all()}
        )


class CourseDetail(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        number = course.course_number
        name = course.course_name
        return render(
            request,
            'courseinfo/course_detail.html',
            {'number': number,
             'name': name}
        )


class CourseCreate(ObjectCreateMixin, View):
    form_class = CourseForm
    template_name = 'courseinfo/course_form.html'



class SemesterList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/semester_list.html',
            {'semester_list': Semester.objects.all()}
        )


class SemesterDetail(View):

    def get(self, request, pk):
        semester = get_object_or_404(Semester, pk=pk)
        section_list = semester.sections.all()
        return render(
            request,
            'courseinfo/semester_detail.html',
            {'semester': semester,
             'section_list': section_list}
        )


class SemesterCreate(ObjectCreateMixin, View):
    form_class = SemesterForm
    template_name = 'courseinfo/semester_form.html'



class StudentList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/student_list.html',
            {'student_list': Student.objects.all()}
        )


class StudentDetail(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return render(
            request,
            'courseinfo/student_detail.html',
            {'student': student}
        )


class StudentCreate(ObjectCreateMixin, View):
    form_class = StudentForm
    template_name = 'courseinfo/student_form.html'



class RegistrationList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/registration_list.html',
            {'registration_list': Registration.objects.all()}
        )


class RegistrationDetail(View):
    def get(self, request, pk):
        registration = get_object_or_404(Registration, pk=pk)
        student = registration.student
        section = registration.section
        return render(
            request,
            'courseinfo/registration_detail.html',
            {'student': student,
             'section': section}
        )


class RegistrationCreate(ObjectCreateMixin, View):
    form_class = RegistrationForm
    template_name = 'courseinfo/registration_form.html'
