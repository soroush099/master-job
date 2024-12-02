from django.urls import path


from profiles.views.contact_info_views import AddressView, ContactInfoView
from profiles.views.register_login_profile_views import CreateUserView, LoginProfileView
from profiles.views.profile_view import ProfileView

urlpatterns = [
    path("register/", CreateUserView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("login/", LoginProfileView.as_view()),
    path("address/", AddressView.as_view()),
    path("contactinfo/", ContactInfoView.as_view()),
]
