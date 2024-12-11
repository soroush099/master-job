from rest_framework import serializers

from profiles.models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "password", "first_name", "last_name", "email")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class PutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "last_name", "email")


class AddressSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Address
        exclude = ("created_date", "updated_date")


class GetContactInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')
    address = AddressSerializer()

    class Meta:
        model = ContactInfo
        exclude = ("created_date", "updated_date")


class CreateContactInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = ContactInfo
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


class JobInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = MyJobInfo
        exclude = ("created_date", "updated_date")
