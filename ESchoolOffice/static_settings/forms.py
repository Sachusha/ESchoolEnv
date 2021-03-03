from django import forms
from .import models


class SchoolProfileForms(forms.ModelForm):
    class Meta:
        model = models.SchoolProfile
        fields = '__all__'

