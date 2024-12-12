from rest_framework import serializers

from profiles.models import ContactInfo
from profiles.serializers.resume_serializers import AddressSerializer


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
