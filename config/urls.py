from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({
        "status": "ok",
        "message": "Todo API is running"
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    path('health/', health_check),
]