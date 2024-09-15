from django.conf import settings
from django.db import models

from profiles.models import ContactInfo, Address


# Create your models here.
class WorkExperience:
    pass


class Education:
    pass


class Skills:
    pass


class CertificateAndProjects:
    pass


class Resume(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    birthday = models.DateTimeField(verbose_name="Birthday")
    gender = models.CharField(verbose_name="Gender")
    marital_status = models.BooleanField(verbose_name="Marital Status", blank=True, null=True)
    job_title = models.CharField(max_length=400, verbose_name="Job Title")
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Address")
    contact_info_id = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, verbose_name="Contact Info")
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name="Work Experience")
    education = models.ForeignKey(Education, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Education")
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Skills")
    certificate_and_projects = models.ForeignKey(CertificateAndProjects, on_delete=models.SET_NULL, blank=True,
                                                 null=True, verbose_name="Certificate And Projects")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")


class JobInfo(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    contact_info_id = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, verbose_name="Contact Info")
    job_title = models.CharField(max_length=400, verbose_name="Job Title")
    description = models.TextField(verbose_name="Description")
    job_certificate = models.FileField(verbose_name="Job Certificate")
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Resume")
