from packages.custom_class_views import GetPostPutDeleteCustomView

from profiles.models import (Resume, WorkExperience, Education, CertificateAndProject, Skill, Address)
from profiles.serializers.resume_serializers import (SkillSerializer,
                                                     ResumeSerializer,
                                                     WorkExperienceSerializer,
                                                     EducationSerializer,
                                                     CertificateAndProjectSerializer,
                                                     ResumeDetailSerializer,
                                                     WorkExperienceDetailSerializer,
                                                     EducationDetailSerializer,
                                                     CertificateAndProjectDetailSerializer,
                                                     CreateResumeSerializer)
from profiles.serializers.contact_info_serializers import (AddressSerializer, AddressDetailSerializer)


class ResumeView(GetPostPutDeleteCustomView):
    model = Resume
    serializer = ResumeSerializer
    create_update_serializer = CreateResumeSerializer
    retrieve_serializer = ResumeDetailSerializer


class AddressView(GetPostPutDeleteCustomView):
    model = Address
    serializer = AddressSerializer
    retrieve_serializer = AddressDetailSerializer


class WorkExperienceView(GetPostPutDeleteCustomView):
    model = WorkExperience
    serializer = WorkExperienceSerializer
    retrieve_serializer = WorkExperienceDetailSerializer


class EducationView(GetPostPutDeleteCustomView):
    model = Education
    serializer = EducationSerializer
    retrieve_serializer = EducationDetailSerializer


class CertificateAndProjectView(GetPostPutDeleteCustomView):
    model = CertificateAndProject
    serializer = CertificateAndProjectSerializer
    retrieve_serializer = CertificateAndProjectDetailSerializer


class SkillView(GetPostPutDeleteCustomView):
    model = Skill
    serializer = SkillSerializer
