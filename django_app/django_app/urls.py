from django.urls import path
from django_app.views import users_view

urlpatterns = [
    path("users", users_view)
]
