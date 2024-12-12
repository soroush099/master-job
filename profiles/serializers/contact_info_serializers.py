from rest_framework import serializers

from profiles.models import ContactInfo, Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "country", "state", "city", "zip_code")


class AddressDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = Address
        exclude = ("created_date", "updated_date")


class GetDetailContactInfoSerializer(serializers.ModelSerializer):
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


class GetContactInfoSerializer(serializers.ModelSerializer):
    address = serializers.StringRelatedField()

    class Meta:
        model = ContactInfo
        fields = ("id", "phone_number", "address", "email_address")
