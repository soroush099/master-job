from django.urls import path
from rest_framework import routers

from job.views.jobs_views import *


router = routers.SimpleRouter()
router.register('', JobsView, basename='jobs')

urlpatterns = [
]

urlpatterns += router.urls
