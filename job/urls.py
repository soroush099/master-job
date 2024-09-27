from django.urls import path

from job.views import ResumeView

urlpatterns = [
    path("resume/", ResumeView.as_view()),
]
