from packages.custom_class_views import GetPostPutDeleteCustomView

from profiles.models import MyJobInfo
from profiles.serializers import JobInfoSerializer


class MyJobInfoView(GetPostPutDeleteCustomView):
    model = MyJobInfo
    serializer = JobInfoSerializer
