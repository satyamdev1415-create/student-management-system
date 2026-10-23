from django.urls import path

from .views import health_check

urlpatterns = [
    path("health/", health_check, name="health-check"),
    # Student, auth and dashboard routes are added in later phases.
]
