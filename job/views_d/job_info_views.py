from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from job.models import JobInfo
from job.serializers import JobInfoSerializer


class JobInfoView(APIView):
    def get(self, request):
        user = request.user
        query = JobInfo.objects.filter(user_id=user.id)
        serializer = JobInfoSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = JobInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        a_id = request.data.get('id')
        query = get_object_or_404(JobInfo, user_id=user.id, pk=a_id)
        serializer = JobInfoSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass
