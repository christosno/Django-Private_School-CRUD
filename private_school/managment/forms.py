from django import forms
from django.forms import widgets
from .models import Trainers, Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_title', 'course_language', 'course_descreption', 'course_type'
        ]

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainers
        fields = [
            'first_name', 'last_name', 'subject', 'courses'
        ]

        widgets = {
            'courses' : forms.SelectMultiple(attrs={
                'size' : '5',
            })
        }

# CheckboxSelectMultiple()