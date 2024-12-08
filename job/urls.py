from django.urls import path

from job.views.resume_views import *
from job.views.job_info_views import *


urlpatterns = [
    path("resume/", ResumeView.as_view()),
    path("resume/workexperience/", WorkExperienceView.as_view()),
    path("resume/education/", EducationView.as_view()),
    path("resume/certificateproject/", CertificateAndProjectView.as_view()),
    path("resume/skill/", SkillView.as_view()),
    path("info/", JobInfoView.as_view()),
]
