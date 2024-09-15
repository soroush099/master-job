from django.conf import settings
from django.db import models

# Create your models here.


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

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.country},{self.state},{self.city}"
