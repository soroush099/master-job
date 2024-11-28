from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from job.models import Resume, WorkExperience, Education, CertificateAndProject
from job.serializers import ResumeSerializer, WorkExperienceSerializer, EducationSerializer, \
    CertificateAndProjectSerializer
from packages.querys import get_query_by_user_id


class ResumeView(APIView):
    def get(self, request):
        return Response(get_query_by_user_id(request, ResumeSerializer, Resume, many_bool=True))

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
        return Response(get_query_by_user_id(request, WorkExperienceSerializer, WorkExperience, many_bool=True))

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
        return Response(get_query_by_user_id(request, EducationSerializer, Education, many_bool=True))

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


class CertificateAndProjectView(APIView):
    def get(self, request):
        return Response(get_query_by_user_id(request, CertificateAndProjectSerializer, CertificateAndProject
                                             , many_bool=True))

    def post(self, request):
        user = request.user
        serializer = CertificateAndProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        a_id = request.data.get('id')
        query = get_object_or_404(CertificateAndProject, user_id=user.id, pk=a_id)
        serializer = CertificateAndProjectSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass