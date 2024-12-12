from rest_framework import serializers

from profiles.models import Address, Skill, Resume, WorkExperience, Education, CertificateAndProject


class AddressSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Address
        exclude = ("created_date", "updated_date")


class SkillSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Skill
        exclude = ("created_date", "updated_date")


class ResumeSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Resume
        exclude = ("created_date", "updated_date")


class WorkExperienceSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = WorkExperience
        exclude = ("created_date", "updated_date")


class EducationSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Education
        exclude = ("created_date", "updated_date")


class CertificateAndProjectSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = CertificateAndProject
        exclude = ("created_date", "updated_date")
