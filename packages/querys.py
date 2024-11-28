def get_query_by_user_id(request, serializer_name, model_name, *, many_bool):
    user = request.user
    query = model_name.objects.filter(user_id=user.id)
    serializer = serializer_name(query, many=many_bool)
    return serializer.data
