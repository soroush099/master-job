from packages.custom_class_views import GetPostPutDeleteAPIView

from profiles.models import ContactInfo
from profiles.serializers import GetContactInfoSerializer


class ContactInfoView(GetPostPutDeleteAPIView):
    model = ContactInfo
    serializer = GetContactInfoSerializer
