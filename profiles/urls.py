from django.urls import path


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

urlpatterns = [
    path("register/", CreateUserView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("login/", LoginProfileView.as_view()),

    path("my-job-info/", MyJobInfoView.as_view()),

    path("resume/", ResumeView.as_view()),
    path("resume/workexperience/", WorkExperienceView.as_view()),
    path("resume/education/", EducationView.as_view()),
    path("resume/certificateproject/", CertificateAndProjectView.as_view()),
    path("resume/skill/", SkillView.as_view()),

    path("address/", AddressView.as_view()),

    path("contactinfo/", ContactsInfoView.as_view()),

]
