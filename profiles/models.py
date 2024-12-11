from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):

    def __str__(self):
        return f'{self.username}'


class Address(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="user")
    country = models.CharField(max_length=255, verbose_name="country")
    state = models.CharField(max_length=255, verbose_name="state")
    city = models.CharField(max_length=255, verbose_name="city")
    district = models.CharField(max_length=255, verbose_name="district")
    street = models.CharField(max_length=255, verbose_name="street")
    alley = models.CharField(max_length=255, verbose_name="alley")
    plate = models.CharField(max_length=255, verbose_name="plate")
    unit = models.CharField(max_length=255, verbose_name="unit")
    zip_code = models.CharField(max_length=100, verbose_name="zip_code")
    description = models.CharField(max_length=400, verbose_name="description")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.country},{self.state},{self.city}"


class ContactInfo(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="user")
    phone_number = models.CharField(max_length=13)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    instagram_account = models.CharField(max_length=300, blank=True, null=True)
    telegram_account = models.CharField(max_length=300, blank=True, null=True)
    linkedin_account = models.CharField(max_length=300, blank=True, null=True)
    website_url = models.CharField(max_length=300, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "ContactInfo"
        verbose_name_plural = "ContactInfos"

    def __str__(self):
        return self.email_address


class WorkExperience(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
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


class Resume(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    birthday = models.DateTimeField(verbose_name="Birthday")
    gender = models.CharField(max_length=400, verbose_name="Gender")
    marital_status = models.BooleanField(verbose_name="Marital Status", blank=True, null=True)
    job_title = models.CharField(max_length=400, verbose_name="Job Title")
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Address")
    contact_info_id = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, verbose_name="Contact Info")
    work_experience = models.ManyToManyField(WorkExperience, blank=True, verbose_name="WorkExperience")
    education = models.ManyToManyField(Education, blank=True, verbose_name="Education")
    skill = models.ManyToManyField(Skill, blank=True, verbose_name="Skill")
    certificate_and_project = models.ManyToManyField(CertificateAndProject, blank=True,
                                                     verbose_name="CertificateAndProject")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return self.job_title


class MyJobInfo(models.Model):
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
