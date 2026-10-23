from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("roll_number", "first_name", "last_name", "email",
                    "course", "department", "semester", "status")
    list_filter = ("status", "course", "department", "semester")
    search_fields = ("roll_number", "first_name", "last_name", "email")
    ordering = ("-created_at",)
