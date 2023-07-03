from django.shortcuts import render, get_object_or_404, redirect
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
        return render(
            request,
            'courseinfo/section_detail.html',
            {'section': section}
        )


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
        return render(
            request,
            'courseinfo/course_detail.html',
            {'course': course}
        )


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
        return render(
            request,
            'courseinfo/semester_detail.html',
            {'semester': semester}
        )


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
        return render(
        request,
        'courseinfo/registration_detail.html',
        {'registration': registration}
        )


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