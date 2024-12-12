from rest_framework import serializers

from profiles.models import (Skill, Resume, WorkExperience, Education, CertificateAndProject)
from profiles.serializers.contact_info_serializers import (AddressDetailSerializer, GetDetailContactInfoSerializer)


class SkillSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Skill
        exclude = ("created_date", "updated_date")


class WorkExperienceDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = WorkExperience
        exclude = ("created_date", "updated_date")


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ("id", "job_title", "company_name")


class EducationDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Education
        exclude = ("created_date", "updated_date")


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("id", "university", "educational_qualifications", "academic_discipline")


class CertificateAndProjectDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = CertificateAndProject
        exclude = ("created_date", "updated_date")


class CertificateAndProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateAndProject
        fields = ("id", "title")


class ResumeDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')
    skill = serializers.StringRelatedField(many=True)
    contact_info_id = GetDetailContactInfoSerializer()
    work_experience = WorkExperienceDetailSerializer(many=True)
    education = EducationDetailSerializer(many=True)
    certificate_and_project = CertificateAndProjectDetailSerializer(many=True)

    class Meta:
        model = Resume
        exclude = ("created_date", "updated_date")


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ("id", "job_title", "description")


class CreateResumeSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Resume
        exclude = ("created_date", "updated_date")
