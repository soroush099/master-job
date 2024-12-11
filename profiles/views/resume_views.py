from packages.custom_class_views import GetPostPutDeleteAPIView

from profiles.models import (Resume, WorkExperience, Education, CertificateAndProject, Skill, Address)
from profiles.serializers import (ResumeSerializer,
                                  WorkExperienceSerializer,
                                  EducationSerializer,
                                  CertificateAndProjectSerializer,
                                  SkillSerializer,
                                  AddressSerializer)


class ResumeView(GetPostPutDeleteAPIView):
    model = Resume
    serializer = ResumeSerializer


class AddressView(GetPostPutDeleteAPIView):
    model = Address
    serializer = AddressSerializer


class WorkExperienceView(GetPostPutDeleteAPIView):
    model = WorkExperience
    serializer = WorkExperienceSerializer


class EducationView(GetPostPutDeleteAPIView):
    model = Education
    serializer = EducationSerializer


class CertificateAndProjectView(GetPostPutDeleteAPIView):
    model = CertificateAndProject
    serializer = CertificateAndProjectSerializer


class SkillView(GetPostPutDeleteAPIView):
    model = Skill
    serializer = SkillSerializer
