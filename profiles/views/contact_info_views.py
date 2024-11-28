from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from packages.querys import get_query_by_user_id
from profiles.models import Address, ContactInfo
from profiles.serializers import AddressSerializer, GetContactInfoSerializer, CreateContactInfoSerializer


class AddressView(APIView):
    def get(self, request):
        return Response(get_query_by_user_id(request, AddressSerializer, Address, many_bool=True))

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


class ContactInfoView(APIView):
    def get(self, request):
        return Response(get_query_by_user_id(request, GetContactInfoSerializer, ContactInfo, many_bool=True))

    def post(self, request):
        user = request.user
        query = Address.objects.filter(user_id=user.id).values_list('id', flat=True)
        serializer = CreateContactInfoSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get('address') in query:
                serializer.save(user_id=user)
                return Response(serializer.data)
            else:
                return Response({"detail": "The address is not correct!"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        contact_id = request.data.get('id')
        query = get_object_or_404(ContactInfo, user_id=user.id, pk=contact_id)
        query_address_id = Address.objects.filter(user_id=user.id).values_list('id', flat=True)
        serializer = CreateContactInfoSerializer(query, data=request.data)
        if serializer.is_valid():
            if request.data.get('address') in query_address_id:
                serializer.save(user_id=user)
                return Response(serializer.data)
            else:
                return Response({"detail": "The address is not correct!"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors)

    def delete(self, request):
        pass
