from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher

        fields = [
            "name",
            "email",
            "phone",
            "subject",
        ]

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if len(name) < 3:
            raise forms.ValidationError(
                "Teacher name must contain at least 3 characters."
            )

        return name


    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()

        if not phone.isdigit():
            raise forms.ValidationError(
                "phone number must contaion only digits"
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "phone number must be exactly 10 digits."
            )

        return phone


    def clean_subject(self):
        subject = self.cleaned_data["subject"].strip()

        if len(subject) < 2:
            raise forms.ValidationError(
                "subject must contain at least 2 charcter."
            )

        return subject 


        