from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.teacher_list,
        name="teacher_list"
    ),

    path(
        "add/",
        views.teacher_create,
        name="teacher_create"
    ),

    path(
        "<int:id>/edit/",
        views.teacher_update,
        name="teacher_update"
    ),

    path(
        "<int:id>/delete/",
        views.teacher_delete,
        name="teacher_delete"
    ),

]