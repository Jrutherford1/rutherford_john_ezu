from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from courseinfo.forms import InstructorForm, SectionForm, CourseForm, SemesterForm, StudentForm, RegistrationForm
from courseinfo.models import Instructor
from courseinfo.models import Section
from courseinfo.models import Course
from courseinfo.models import Semester
from courseinfo.models import Student
from courseinfo.models import Registration
from courseinfo.utils import ObjectCreateMixin, PageLinksMixin


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


class InstructorCreate(ObjectCreateMixin, View):
    form_class = InstructorForm
    template_name = 'courseinfo/instructor_form.html'


class InstructorUpdate(View):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        instructor = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=instructor),
            'instructor': instructor,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        instructor = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=instructor)
        if bound_form.is_valid():
            new_instructor = bound_form.save()
            return redirect(new_instructor)
        else:
            context = {
                'form': bound_form,
                'instructor': instructor,
            }
            return render(
                request,
                self.template_name,
                context)


class InstructorDelete(View):

    def get(self, request, pk):
        instructor = self.get_object(pk)
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

    def get_object(self, pk):
        return get_object_or_404(
            Instructor,
            pk=pk)

    def post(self, request, pk):
        instructor = self.get_object(pk)
        instructor.delete()
        return redirect('courseinfo_instructor_list_urlpattern')


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


class SectionCreate(ObjectCreateMixin, View):
    form_class = SectionForm
    template_name = 'courseinfo/section_form.html'


class SectionUpdate(View):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        section = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=section),
            'section': section,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        section = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=section)
        if bound_form.is_valid():
            new_section = bound_form.save()
            return redirect(new_section)
        else:
            context = {
                'form': bound_form,
                'section': section,
            }
            return render(
                request,
                self.template_name,
                context)


class SectionDelete(View):

    def get(self, request, pk):
        section = self.get_object(pk)
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

    def get_object(self, pk):
        return get_object_or_404(
            Section,
            pk=pk
        )

    def post(self, request, pk):
        section = self.get_object(pk)
        section.delete()
        return redirect('courseinfo_section_list_urlpattern')


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


class CourseCreate(ObjectCreateMixin, View):
    form_class = CourseForm
    template_name = 'courseinfo/course_form.html'


class CourseUpdate(View):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        course = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=course),
            'course': course,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        course = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=course)
        if bound_form.is_valid():
            new_course = bound_form.save()
            return redirect(new_course)
        else:
            context = {
                'form': bound_form,
                'course': course,
            }
            return render(
                request,
                self.template_name,
                context)


class CourseDelete(View):

    def get(self, request, pk):
        course = self.get_object(pk)
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

    def get_object(self, pk):
        return get_object_or_404(
            Course,
            pk=pk)

    def post(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return redirect('courseinfo_course_list_urlpattern')


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


class SemesterCreate(ObjectCreateMixin, View):
    form_class = SemesterForm
    template_name = 'courseinfo/semester_form.html'


class SemesterUpdate(View):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        semester = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=semester),
            'semester': semester,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        semester = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=semester)
        if bound_form.is_valid():
            new_semester = bound_form.save()
            return redirect(new_semester)
        else:
            context = {
                'form': bound_form,
                'semester': semester,
            }
            return render(
                request,
                self.template_name,
                context)


class SemesterDelete(View):

    def get(self, request, pk):
        semester = self.get_object(pk)
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

    @staticmethod
    def get_object(pk):
        semester = get_object_or_404(
            Semester,
            pk=pk
        )
        return semester

    def post(self, request, pk):
        semester = self.get_object(pk)
        semester.delete()
        return redirect('courseinfo_semester_list_urlpattern')


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


class StudentCreate(ObjectCreateMixin, View):
    form_class = StudentForm
    template_name = 'courseinfo/student_form.html'


class StudentUpdate(View):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=student),
            'student': student,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        student = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=student)
        if bound_form.is_valid():
            new_student = bound_form.save()
            return redirect(new_student)
        else:
            context = {
                'form': bound_form,
                'student': student,
            }
            return render(
                request,
                self.template_name,
                context)


class StudentDelete(View):

    def get(self, request, pk):
        student = self.get_object(pk)
        registrations = student.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/student_refuse_delete.html',
                {'student': student,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/student_confirm_delete.html',
                {'student': student}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Student,
            pk=pk)

    def post(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return redirect('courseinfo_student_list_urlpattern')


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


class RegistrationCreate(ObjectCreateMixin, View):
    form_class = RegistrationForm
    template_name = 'courseinfo/registration_form.html'


class RegistrationUpdate(View):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        registration = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=registration),
            'registration': registration,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        registration = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=registration)
        if bound_form.is_valid():
            new_registration = bound_form.save()
            return redirect(new_registration)
        else:
            context = {
                'form': bound_form,
                'registration': registration,
            }
            return render(
                request,
                self.template_name,
                context)


class RegistrationDelete(View):

    def get(self, request, pk):
        registration = self.get_object(pk)
        return render(
            request,
            'courseinfo/registration_confirm_delete.html',
            {'registration': registration}
        )

    def get_object(self, pk):
        registration = get_object_or_404(
            Registration,
            pk=pk
        )
        return registration

    def post(self, request, pk):
        registration = self.get_object(pk)
        registration.delete()
        return redirect('courseinfo_registration_list_urlpattern')
