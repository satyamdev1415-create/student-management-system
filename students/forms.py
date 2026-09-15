from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "name",
            "email",
            "phone",
            "gender",
            "date_of_birth",
            "address",
            "roll_number",
            "course",
        ]

    def clean_name(self):
        name = self.cleaned_data["name"]

        name = name.strip()

        if len(name) < 3:
            raise forms.ValidationError(
                "Name must contain at least 3 characters."
            )

        return name

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        phone = phone.strip()

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number must contain only digits."
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )

        return phone

    def clean_roll_number(self):
        roll_number = self.cleaned_data["roll_number"]

        roll_number = roll_number.strip()

        if not roll_number:
            raise forms.ValidationError(
                "Roll number is required."
            )

        return roll_number