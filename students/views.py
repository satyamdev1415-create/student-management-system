from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from courses.models import Course

from django.contrib import messages



@login_required
def student_list(request):

    search = request.GET.get("q", "")
    course_id = request.GET.get("course", "")

    students = Student.objects.all()

    # Search by student name
    if search:
        students = students.filter(
            name__icontains=search
        )

    # Filter by course
    if course_id:
        students = students.filter(
            course_id=course_id
        )

    # Courses for filter dropdown
    courses = Course.objects.all()

    # Pagination
    paginator = Paginator(students, 5)

    page_number = request.GET.get("page")

    students = paginator.get_page(page_number)

    return render(
        request,
        "students/student_list.html",
        {
            "students": students,
            "search": search,
            "courses": courses,
            "selected_course": course_id,
        }
    )



@login_required
def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )



@login_required
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )




@login_required
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {
            "form":form,
            "student":student
        }
    )

@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        
        return redirect("student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )