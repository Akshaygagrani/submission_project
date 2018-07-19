from django import forms
from .models import info

class add_student(forms.ModelForm):

    class Meta:
        model = info
        fields = ('first_name', 'last_name', 'year', 'message')
