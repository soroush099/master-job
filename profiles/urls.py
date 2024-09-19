from django.urls import path

from profiles.views import *

urlpatterns = [
    path("register/", CreateUserView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("login/", LoginProfileView.as_view()),
    path("address/", AddressView.as_view()),
    path("contactinfo/", ContactInfoView.as_view()),
]
