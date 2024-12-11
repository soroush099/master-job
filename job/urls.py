from django.urls import path
from rest_framework import routers

from job.views.jobs_list_views import *


router = routers.SimpleRouter()
router.register('', JobsListView, basename='jobs')

urlpatterns = [
]

urlpatterns += router.urls
