from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clean-data", views.clean_data, name="clean-data"),
    path("log-in", views.log_in, name="log-in"),
    path("sign-up", views.sign_up, name="sign-up"),
    path("logout", views.logout_user, name="logout"),
]
