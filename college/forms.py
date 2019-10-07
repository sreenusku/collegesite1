"""
    this is forms module for college app
"""
from django import forms
from .models import StudentRegistration


class StudentApplication(forms.Form):
    """
        here we are declaring student application form fields
    """
    student_name = forms.CharField(max_length=100)
    email = forms.EmailField(unique=True)                      # for showing & validating  in html
    dob = forms.DateTimeField()
    ssc_doc = forms.FileField()
    inter_doc = forms.FileField()


class StudentRegistrationForm(forms.ModelForm):
    """
        here we are declaring student registration form fields
    """
    class Meta:
        """
            here we are declaring Meta class for student registration
        """
        model = StudentRegistration
        fields = ('application', 'user', 'dob', 'father_name', 'mother_name', 'profile_pic',
                  'gender', 'nationality', 'department', 'is_student')

        # this data will go and stored in StudentRegistration table in the models.
