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