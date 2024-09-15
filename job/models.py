from django.conf import settings
from django.db import models

from profiles.models import ContactInfo


# Create your models here.
class Resume(models.Model):
    pass


class JobInfo(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    contact_info_id = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, verbose_name="Contact Info")
    job_title = models.CharField(max_length=400, verbose_name="Job Title")
    description = models.TextField(verbose_name="Description")
    job_certificate = models.FileField(verbose_name="Job Certificate")
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Resume")
