from django.urls import path

from .views import website, coin

urlpatterns = [
    path('', coin.home, name="home"),

    path('logout/', website.logout_user, name="logout"),
    path('profile/', website.profile, name="profile"),
    path('update_profile/', website.update_profile, name="update-profile"),
]