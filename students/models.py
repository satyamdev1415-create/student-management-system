from django.db import models
from courses.models import Course


class Student(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    date_of_birth = models.DateField()
    address = models.TextField()
    roll_number = models.CharField(
        max_length=50,
        unique=True
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name