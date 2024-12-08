from job.models import Resume, WorkExperience, Education, CertificateAndProject
from packages.custom_class_views import GetPostPutDeleteAPIView
from job.serializers import (ResumeSerializer,
                             WorkExperienceSerializer,
                             EducationSerializer,
                             CertificateAndProjectSerializer)


class ResumeView(GetPostPutDeleteAPIView):
    model = Resume
    serializer = ResumeSerializer

    
class WorkExperienceView(GetPostPutDeleteAPIView):
    model = WorkExperience
    serializer = WorkExperienceSerializer


class EducationView(GetPostPutDeleteAPIView):
    model = Education
    serializer = EducationSerializer


class CertificateAndProjectView(GetPostPutDeleteAPIView):
    model = CertificateAndProject
    serializer = CertificateAndProjectSerializer
