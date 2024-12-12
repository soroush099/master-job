from packages.custom_class_views import GetPostPutDeleteCustomView

from profiles.models import (Resume, WorkExperience, Education, CertificateAndProject, Skill, Address)
from profiles.serializers import (ResumeSerializer,
                                  WorkExperienceSerializer,
                                  EducationSerializer,
                                  CertificateAndProjectSerializer,
                                  SkillSerializer,
                                  AddressSerializer)


class ResumeView(GetPostPutDeleteCustomView):
    model = Resume
    serializer = ResumeSerializer


class AddressView(GetPostPutDeleteCustomView):
    model = Address
    serializer = AddressSerializer


class WorkExperienceView(GetPostPutDeleteCustomView):
    model = WorkExperience
    serializer = WorkExperienceSerializer


class EducationView(GetPostPutDeleteCustomView):
    model = Education
    serializer = EducationSerializer


class CertificateAndProjectView(GetPostPutDeleteCustomView):
    model = CertificateAndProject
    serializer = CertificateAndProjectSerializer


class SkillView(GetPostPutDeleteCustomView):
    model = Skill
    serializer = SkillSerializer
