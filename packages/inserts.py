def post_insert_and_change_user_id(request, serializer_name, ):
    user = request.user
    serializer = serializer_name(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['user_id'] = user
        serializer.save()
        return serializer.data
    return serializer.errors