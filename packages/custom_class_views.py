from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


class GetPostPutDeleteAPIView(APIView):
    model = None
    serializer = None
    post_put_serializer = serializer
    many_bool = True

    def get(self, request):
        user = request.user
        query = self.model.objects.filter(user_id=user.id)
        serializer = self.serializer(query, many=self.many_bool)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = self.post_put_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        user = request.user
        a_id = request.data.get('id')
        query = get_object_or_404(self.model, user_id=user.id, pk=a_id)
        serializer = self.post_put_serializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass
