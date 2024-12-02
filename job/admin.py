from django.contrib import admin

from job.models import *


# Register your models here.


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "job_title", "user_id")


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(CertificateAndProject)
class CertificateAndProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(JobInfo)
class JobInfoAdmin(admin.ModelAdmin):
    pass
