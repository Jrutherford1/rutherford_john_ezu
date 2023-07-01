from django import forms

from courseinfo.models import Instructor
from courseinfo.models import Section
from courseinfo.models import Course
from courseinfo.models import Semester
from courseinfo.models import Student
from courseinfo.models import Registration


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

        def clean_first_name(self):
            return self.cleaned_data['first_name'].strip()

        def clean_last_name(self):
            return self.cleaned_data['last_name'].strip()

        def clean_disambiguator(self):
            if len(self.cleaned_data['disambiguator']) == 0:
                result = self.cleaned_data['disambiguator']
            else:
                result = self.cleaned_data['disambiguator'].strip()
            return result


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

        def clean_section_name(self):
            return self.cleaned_data['section_name'].strip()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        def clean_course_number(self):
            return self.cleaned_data['course_number'].strip()

        def clean_course_name(self):
            return self.cleaned_data['course_name'].strip()


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'

        def clean_semester_year(self):
            return self.cleaned_data['semester_year'].strip()

        def clean_semester_period(self):
            return self.cleaned_data['semester_period'].strip()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        def clean_first_name(self):
            return self.cleaned_data['first_name'].strip()

        def clean_last_name(self):
            return self.cleaned_data['last_name'].strip()

        def clean_disambiguator(self):
            if len(self.cleaned_data['disambiguator']) == 0:
                result = self.cleaned_data['disambiguator']
            else:
                result = self.cleaned_data['disambiguator'].strip()
            return result


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

        def clean_semester_year(self):
            return self.cleaned_data['student'].strip()

        def clean_semester_period(self):
            return self.cleaned_data['section'].strip()

