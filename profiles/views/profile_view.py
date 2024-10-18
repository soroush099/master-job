from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import CustomUser
from profiles.serializers import CustomUserSerializer, PutUserSerializer


class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        query = CustomUser.objects.get(pk=user.id)
        serializer = CustomUserSerializer(query)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        query = CustomUser.objects.get(pk=user.id)
        serializer = PutUserSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
