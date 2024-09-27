from django.urls import path

from job.views import *

urlpatterns = [
    path("resume/", ResumeView.as_view()),
    path("resume/workexperience/", WorkExperienceView.as_view()),
    path("resume/education/", EducationView.as_view()),
]
