from job.models import JobInfo
from job.serializers import JobInfoSerializer

from packages.custom_class_views import GetPostPutDeleteAPIView


class JobInfoView(GetPostPutDeleteAPIView):
    model = JobInfo
    serializer = JobInfoSerializer
