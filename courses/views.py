from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from  .forms import CourseForm
from django.core.paginator import Paginator


from django.contrib.auth.decorators import login_required



@login_required
def course_list(request):

    search = request.GET.get("q", "")

    courses = Course.objects.all()

    if search:
        courses = courses.filter(
            name__icontains=search
        )

    paginator = Paginator(courses, 5)

    page_number = request.GET.get("page")

    courses = paginator.get_page(page_number) 


    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses,
            "search": search,
        }
    )



@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm()


    return render(request, "courses/course_form.html", {"form":form})


@login_required
def course_update(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "courses/course_form.html",
        {
            "form": form,
            "course": course
        }
    )

@login_required
def course_delete(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(
        request,
        "courses/course_confirm_delete.html",
        {"course": course}
    )