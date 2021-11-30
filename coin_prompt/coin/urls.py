from django.urls import path

from .views import create_alert, delete_alert

urlpatterns = [
    path('create_alert/', create_alert, name="create-alert"),
    path('delete_alert/', delete_alert, name="delete-alert")
]