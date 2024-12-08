from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from job.models import JobInfo
from job.serializers import JobInfoSerializer
from packages.inserts import post_insert, put_insert
from packages.querys import get_query_by_user_id


class JobInfoView(APIView):
    def get(self, request):
        return Response(get_query_by_user_id(request, JobInfoSerializer, JobInfo, many_bool=True))

    def post(self, request):
        return Response(post_insert(request, JobInfoSerializer))

    def put(self, request):
        return Response(put_insert(request, JobInfo, JobInfoSerializer))

    def delete(self, request):
        pass
