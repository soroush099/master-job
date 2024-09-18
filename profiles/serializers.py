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

