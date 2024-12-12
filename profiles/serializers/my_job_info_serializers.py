from rest_framework import serializers

from profiles.models import MyJobInfo


class JobInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default='user_id')

    class Meta:
        model = MyJobInfo
        exclude = ("created_date", "updated_date")
