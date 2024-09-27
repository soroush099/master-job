from rest_framework import serializers

from job.models import *


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
