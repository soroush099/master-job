from django.contrib import admin

from profiles.models import *


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    pass
