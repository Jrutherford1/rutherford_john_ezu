from django import forms

from courseinfo.models import Instructor


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

