from django import forms
from .models import Course



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "description",]


    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "Course name must contain at least 2 charcter"
            )

        return name










