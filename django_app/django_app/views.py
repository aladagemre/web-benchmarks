from django.http import JsonResponse
from django_app.models import User

def users_view(request):
    count = User.objects.count()
    return JsonResponse({"count": count})
