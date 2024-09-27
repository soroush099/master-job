from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from job.models import Resume, WorkExperience, Education
from job.serializers import ResumeSerializer, WorkExperienceSerializer, EducationSerializer


# Create your views here.


class ResumeView(APIView):
    def get(self, request):
        user = request.user
        query = Resume.objects.filter(user_id=user.id)
        serializer = ResumeSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        a_id = request.data.get('id')
        query = get_object_or_404(Resume, user_id=user.id, pk=a_id)
        serializer = ResumeSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass


class WorkExperienceView(APIView):
    def get(self, request):
        user = request.user
        query = WorkExperience.objects.filter(user_id=user.id)
        serializer = WorkExperienceSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = WorkExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        a_id = request.data.get('id')
        query = get_object_or_404(WorkExperience, user_id=user.id, pk=a_id)
        serializer = WorkExperienceSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass


class EducationView(APIView):
    def get(self, request):
        user = request.user
        query = Education.objects.filter(user_id=user.id)
        serializer = EducationSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        a_id = request.data.get('id')
        query = get_object_or_404(Education, user_id=user.id, pk=a_id)
        serializer = EducationSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass
