from rest_framework import serializers

from profiles.models import MyJobInfo


class JobInfoDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = MyJobInfo
        exclude = ("created_date", "updated_date")


class JobInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyJobInfo
        fields = ("id", "job_title")
