from packages.custom_class_views import GetPostPutDeleteCustomView

from profiles.models import ContactInfo
from profiles.serializers.contact_info_serializers import (GetContactInfoSerializer,
                                                           CreateContactInfoSerializer,
                                                           GetDetailContactInfoSerializer)


class ContactsInfoView(GetPostPutDeleteCustomView):
    model = ContactInfo
    serializer = GetContactInfoSerializer
    create_update_serializer = CreateContactInfoSerializer
    retrieve_serializer = GetDetailContactInfoSerializer
