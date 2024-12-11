from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from job.models import RequestedJobInformation
from job.serializers import RequestedJobInformationSerializer


class JobsListView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request):
        queryset = RequestedJobInformation.objects.all()
        serializer = RequestedJobInformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        query = get_object_or_404(RequestedJobInformation, pk=pk)
        serializer = RequestedJobInformationSerializer(query)
        return Response(serializer.data)
