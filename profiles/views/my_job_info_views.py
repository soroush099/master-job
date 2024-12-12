from packages.custom_class_views import GetPostPutDeleteCustomView

from profiles.models import MyJobInfo
from profiles.serializers.my_job_info_serializers import JobInfoSerializer


class MyJobInfoView(GetPostPutDeleteCustomView):
    model = MyJobInfo
    serializer = JobInfoSerializer
