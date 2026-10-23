from django.db import connection
from django.http import JsonResponse


def health_check(request):
    """Used by Render/uptime monitors. Also confirms the database is reachable."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "ok", "database": "ok"})
    except Exception:
        return JsonResponse({"status": "error", "database": "unreachable"}, status=503)
