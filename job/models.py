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
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return self.job_title


class WorkExperience(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    resume = models.ManyToManyField(Resume, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name="Resume")
    job_title = models.CharField(max_length=400, verbose_name="Job Title")
    company_name = models.CharField(max_length=400, verbose_name="Company Name")
    start_date = models.DateTimeField(verbose_name="Start Date")
    end_date = models.DateTimeField(verbose_name="End Date")
    responsibilities = models.TextField(verbose_name="Responsibilities", blank=True, null=True)
    achievements = models.TextField(verbose_name="Achievements", blank=True, null=True)
    descriptions = models.TextField(verbose_name="Description", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "WorkExperience"
        verbose_name_plural = "WorkExperiences"

    def __str__(self):
        return self.job_title


class Education(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    resume = models.ManyToManyField("Education", on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name="Resume")
    educational_qualifications = models.CharField(max_length=500, verbose_name="Educational Qualifications")
    academic_discipline = models.CharField(max_length=500, verbose_name="Academic Discipline")
    university = models.CharField(max_length=500, verbose_name="University")
    university_location = models.CharField(max_length=500, verbose_name="University Location")
    start_date = models.DateTimeField(verbose_name="Start Date")
    end_date = models.DateTimeField(verbose_name="End Date", blank=True, null=True)
    descriptions = models.TextField(verbose_name="Description", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return self.educational_qualifications


class Skill(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    resume = models.ManyToManyField(Resume, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="resume")
    skill_text = models.CharField(max_length=400, verbose_name="Skill Text")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.skill_text


class CertificateAndProject(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    resume = models.ManyToManyField(Resume, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Resume")
    title = models.CharField(max_length=500, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    start_date = models.DateTimeField(verbose_name="Start Date")
    end_date = models.DateTimeField(verbose_name="End Date", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "CertificateAndProject"
        verbose_name_plural = "CertificatesAndProjects"

    def __str__(self):
        return self.title


class JobInfo(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    contact_info_id = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, verbose_name="Contact Info")
    job_title = models.CharField(max_length=400, verbose_name="Job Title")
    description = models.TextField(verbose_name="Description")
    job_certificate = models.FileField(verbose_name="Job Certificate")
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Resume")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "JobInfo"
        verbose_name_plural = "JobInfo"

    def __str__(self):
        return self.job_title
