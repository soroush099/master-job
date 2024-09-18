from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import *
from profiles.serializers import CustomUserSerializer, PutUserSerializer, AddressSerializer


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


class LoginProfileView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class AddressView(APIView):
    def get(self, request):
        user = request.user
        query = Address.objects.filter(user_id=user.id)
        serializers = AddressSerializer(query, many=True)
        return Response(serializers.data)

    def post(self, request):
        user = request.user
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        a_id = request.data.get('id')
        # query = Address.objects.filter(user_id=user.id).get(pk=a_id)
        query = get_object_or_404(Address, user_id=user.id, pk=a_id)
        serializer = AddressSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass
