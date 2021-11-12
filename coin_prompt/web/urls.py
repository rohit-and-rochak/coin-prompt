from django.urls import path

from .views import website

urlpatterns = [
    path('', website.home)
]