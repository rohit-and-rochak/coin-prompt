from django.urls import path

from .views import create_alert

urlpatterns = [
    path('create_alert/', create_alert, name="create-alert")
]