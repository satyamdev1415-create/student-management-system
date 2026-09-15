from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required
def teacher_list(request):

    search = request.GET.get("q", "")
    subject = request.GET.get("subject", "")

    teachers = Teacher.objects.all()

    
    if search:
        teachers = teachers.filter(
            name__icontains=search
        )

    
    if subject:
        teachers = teachers.filter(
            subject__iexact=subject
        )

    
    subjects = (
        Teacher.objects
        .values_list("subject", flat=True)
        .distinct()
        .order_by("subject")
    )

    
    paginator = Paginator(teachers, 5)

    page_number = request.GET.get("page")

    teachers = paginator.get_page(page_number)

    return render(
        request,
        "teachers/teacher_list.html",
        {
            "teachers": teachers,
            "search": search,
            "subjects": subjects,
            "selected_subject": subject,
        }
    )



@login_required
def teacher_create(request):

    if request.method == "POST":

        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("teacher_list")

    else:

        form = TeacherForm()

    return render(
        request,
        "teachers/teacher_form.html",
        {"form": form}
    )

@login_required
def teacher_update(request, id):
    teacher = get_object_or_404( Teacher, id=id)

    if request.method == "POST":
        form = TeacherForm( request.POST, instance=teacher )
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    else:
        form = TeacherForm(instance=teacher)

    return render(request,"teachers/teacher_form.html",
        {
            "form": form,
            "teacher": teacher
        }
    )

@login_required
def teacher_delete(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":
        teacher.delete()
        return redirect("teacher_list")

    return render(
        request,
        "teachers/teacher_confirm_delete.html",
        {"teacher": teacher}
    )




















