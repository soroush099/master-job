from django.urls import path
from rest_framework import routers

from profiles.views.contact_info_views import ContactsInfoView
from profiles.views.my_job_info_views import MyJobInfoView
from profiles.views.register_login_profile_views import CreateUserView, LoginProfileView
from profiles.views.profile_view import ProfileView
from profiles.views.resume_views import (ResumeView,
                                         WorkExperienceView,
                                         EducationView,
                                         CertificateAndProjectView,
                                         SkillView,
                                         AddressView)


router = routers.SimpleRouter()
router.register("address", AddressView, basename="address")
router.register("my-job-info", MyJobInfoView, basename="my-job-info")
router.register("contactinfo", ContactsInfoView, basename="contactinfo")
router.register("resume", ResumeView, basename="resume")
router.register("resume-workexperience", WorkExperienceView, basename="workexperience")
router.register("resume-education", EducationView, basename="education")
router.register("resume-certificateproject", CertificateAndProjectView, basename="certificateproject")
router.register("resume-skill", SkillView, basename="skill")

urlpatterns = [
    path("register/", CreateUserView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("login/", LoginProfileView.as_view()),
]
urlpatterns += router.urls
