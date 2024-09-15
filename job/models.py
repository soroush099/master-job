from django.conf import settings
from django.db import models

from profiles.models import ContactInfo, Address


# Create your models here.


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
    skills = models.ManyToManyField("Skills", on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name="Skills")
    certificate_and_projects = models.ManyToManyField("CertificateAndProjects", on_delete=models.SET_NULL,
                                                      blank=True, null=True, verbose_name="Certificate And Projects")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")


class WorkExperience:
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    resume = models.ManyToManyField(Resume, on_delete=models.SET_NULL, blank=True, null=True,
                                             verbose_name="Work Experience")
    job_title = models.CharField(max_length=400, verbose_name="Job Title")
    company_name = models.CharField(max_length=400, verbose_name="Company Name")
    start_date = models.DateTimeField(verbose_name="Start Date")
    end_date = models.DateTimeField(verbose_name="End Date")
    responsibilities = models.TextField(verbose_name="Responsibilities", blank=True, null=True)
    achievements = models.TextField(verbose_name="Achievements", blank=True, null=True)
    descriptions = models.TextField(verbose_name="Description", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")


class Education:
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    education = models.ManyToManyField("Education", on_delete=models.SET_NULL, blank=True, null=True,
                                       verbose_name="Education")
    educational_qualifications = models.CharField(max_length=500, verbose_name="Educational Qualifications")
    academic_discipline = models.CharField(max_length=500, verbose_name="Academic Discipline")
    university = models.CharField(max_length=500, verbose_name="University")
    university_location = models.CharField(max_length=500, verbose_name="University Location")
    start_date = models.DateTimeField(verbose_name="Start Date")
    end_date = models.DateTimeField(verbose_name="End Date", blank=True, null=True)
    descriptions = models.TextField(verbose_name="Description", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")


class Skills:
    pass


class CertificateAndProjects:
    pass


class JobInfo(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    contact_info_id = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, verbose_name="Contact Info")
    job_title = models.CharField(max_length=400, verbose_name="Job Title")
    description = models.TextField(verbose_name="Description")
    job_certificate = models.FileField(verbose_name="Job Certificate")
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Resume")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
