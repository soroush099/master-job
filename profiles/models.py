from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    pass


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
        return self.user_id

