from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import CustomUser
from profiles.serializers import CustomUserSerializer, PutUserSerializer


# Create your views here.

class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            response_data = {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'token': token.key,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

