from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from students.models import Student
from teachers.models import Teacher
from courses.models import Course


@login_required
def dashboard(request):

    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    course_count = Course.objects.count()

    recent_students = Student.objects.all().order_by("-id")[:5]

    recent_teachers = Teacher.objects.all().order_by("-id")[:5]

    recent_courses = Course.objects.all().order_by("-id")[:5]


    course_overview = Course.objects.annotate(
        student_total=Count("students")
    ).order_by("-student_total")

    context = {

        "student_count": student_count,
        "teacher_count": teacher_count,
        "course_count": course_count,

        "recent_students": recent_students,
        "recent_teachers": recent_teachers,
        "recent_courses": recent_courses,

        "course_overview": course_overview,
    }


    return render(
        request,
        "dashboard/dashboard.html",
        context
    )




def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")


        if password != confirm_password:

            return render(
                request,
                "registration/register.html",
                {
                    "error": "Passwords do not match"
                }
            )


        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        return redirect("login")


    return render(
        request,
        "registration/register.html"
    )