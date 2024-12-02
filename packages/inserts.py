from django.shortcuts import get_object_or_404


def post_insert_and_change_user_id(request, serializer_name, ):
    user = request.user
    serializer = serializer_name(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['user_id'] = user
        serializer.save()
        return serializer.data
    return serializer.errors


def put_insert_and_change_user_id(request, model_name, serializer_name):
    user = request.user
    a_id = request.data.get('id')
    query = get_object_or_404(model_name, user_id=user.id, pk=a_id)
    serializer = serializer_name(query, data=request.data)
    if serializer.is_valid():
        serializer.save(user_id=user)
        return serializer.data
    return serializer.errors
