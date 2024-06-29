from django.db import models
from datetime import datetime
# Create your models here.
class Enquiry(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    source_of_Enquiry = models.CharField(max_length=200, default='website')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Enquiries"


class MarketAppraisal(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    cars = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Market Appraisals"