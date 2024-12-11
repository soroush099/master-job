from packages.custom_class_views import GetPostPutDeleteAPIView

from profiles.models import MyJobInfo
from profiles.serializers import JobInfoSerializer


class MyJobInfoView(GetPostPutDeleteAPIView):
    model = MyJobInfo
    serializer = JobInfoSerializer
