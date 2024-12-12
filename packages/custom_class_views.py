from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets


class GetPostPutDeleteCustomView(viewsets.ViewSet):
    model = None
    serializer = None
    create_update_serializer = None
    retrieve_serializer = None

    def serializer_selection(self):
        if self.create_update_serializer is None:
            if self.retrieve_serializer is None:
                self.create_update_serializer = self.serializer
            else:
                self.create_update_serializer = self.retrieve_serializer
        if self.retrieve_serializer is None:
            self.retrieve_serializer = self.serializer

    def list(self, request):
        print(request)
        user = request.user
        query = self.model.objects.filter(user_id=user.id)
        serializer = self.serializer(query, many=True)
        return Response(serializer.data)

    def create(self, request):
        self.serializer_selection()
        user = request.user
        serializer = self.create_update_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = user
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        self.serializer_selection()
        user = request.user
        query = get_object_or_404(self.model, user_id=user.id, pk=pk)
        serializer = self.retrieve_serializer(query)
        return Response(serializer.data)

    def update(self, request, pk=None):
        self.serializer_selection()
        user = request.user
        query = get_object_or_404(self.model, user_id=user.id, pk=pk)
        serializer = self.create_update_serializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user)
            return Response(serializer.data)
        return Response(serializer.errors)

    # def destroy(self, request, pk=None):
    #     pass
