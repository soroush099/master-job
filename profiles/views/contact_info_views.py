from packages.custom_class_views import GetPostPutDeleteAPIView

from profiles.models import ContactInfo
from profiles.serializers import GetContactInfoSerializer, CreateContactInfoSerializer


class ContactsInfoView(GetPostPutDeleteAPIView):
    model = ContactInfo
    serializer = GetContactInfoSerializer
    post_put_serializer = CreateContactInfoSerializer
