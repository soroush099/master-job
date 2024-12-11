from rest_framework import serializers

from job.models import *


class RequestedJobInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedJobInformation
        exclude = ()
