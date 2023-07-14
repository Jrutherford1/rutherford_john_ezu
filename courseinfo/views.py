from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from courseinfo.forms import InstructorForm, SectionForm, CourseForm, SemesterForm, StudentForm, RegistrationForm
from courseinfo.models import Instructor
from courseinfo.models import Section
from courseinfo.models import Course
from courseinfo.models import Semester
from courseinfo.models import Student
from courseinfo.models import Registration
from courseinfo.utils import PageLinksMixin


class InstructorList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Instructor


class InstructorDetail(DetailView):
    model = Instructor

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        instructor = self.get_object()
        section_list = instructor.sections.all()
        context['section_list'] = section_list
        return context


class InstructorCreate(CreateView):
    form_class = InstructorForm
    model = Instructor


class InstructorUpdate(UpdateView):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'


class InstructorDelete(DeleteView):
    model = Instructor
    success_url = reverse_lazy('courseinfo_instructor_list_urlpattern')

    def get(self, request, pk):
        instructor = get_object_or_404(Instructor, pk=pk)
        sections = instructor.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/instructor_refuse_delete.html',
                {'instructor': instructor,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/instructor_confirm_delete.html',
                {'instructor': instructor}
            )


class SectionList(ListView):
    model = Section
    permission_required = 'courseinfo.view_section'


class SectionDetail(DetailView):
    model = Section

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        section = self.get_object()
        course = section.course
        semester = section.semester
        instructor = section.instructor
        registration_list = section.registrations.all()
        context['semester'] = semester
        context['course'] = course
        context['instructor'] = instructor
        context['registration_list'] = registration_list
        return context


class SectionCreate(CreateView):
    form_class = SectionForm
    model = Section


class SectionUpdate(UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'


class SectionDelete(DeleteView):
    model = Section
    success_url = reverse_lazy('courseinfo_section_list_urlpattern')

    def get(self, request, pk):
        section = self.get_object()
        registrations = section.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/section_refuse_delete.html',
                {'section': section,
                'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/section_confirm_delete.html',
                {'section': section}
            )


class CourseList(ListView):
    model = Course
    permission_required = 'courseinfo.view_course'


class CourseDetail(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        section_list = course.sections.all()
        context['section_list'] = section_list
        return context


class CourseCreate(CreateView):
    form_class = CourseForm
    model = Course


class CourseUpdate(UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courseinfo_course_list_urlpattern')

    def get(self, request, pk):
        course = self.get_object()
        sections = course.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )


class SemesterList(ListView):
    model = Semester
    permission_required = 'courseinfo.view_semester'


class SemesterDetail(DetailView):
    model = Semester

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        semester = self.get_object()
        section_list = semester.sections.all()
        context['section_list'] = section_list
        return context


class SemesterCreate(CreateView):
    form_class = SemesterForm
    model = Semester


class SemesterUpdate(UpdateView):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'


class SemesterDelete(DeleteView):
    model = Semester
    success_url = reverse_lazy('courseinfo_semester_list_urlpattern')

    def get(self, request, pk):
        semester = self.get_object()
        sections = semester.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/semester_refuse_delete.html',
                {'semester': semester,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/semester_confirm_delete.html',
                {'semester': semester}
            )


class StudentList(PageLinksMixin, ListView):
    paginate_by = 25
    model = Student


class StudentDetail(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        student = self.get_object()
        registration_list = student.registrations.all()
        context['registration_list'] = registration_list
        return context


class StudentCreate(CreateView):
    form_class = StudentForm
    model = Student


class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('courseinfo_student_list_urlpattern')


class RegistrationList(ListView):
    model = Registration
    permission_required = 'courseinfo.view_registration'


class RegistrationDetail(DetailView):
    model = Registration

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        registration = self.get_object()
        section = registration.section
        student = registration.student
        registration = registration
        context['section'] = section
        context['student'] = student
        context['registration'] = registration
        return context


class RegistrationCreate(CreateView):
    form_class = RegistrationForm
    model = Registration


class RegistrationUpdate(UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'


class RegistrationDelete(DeleteView):
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')

