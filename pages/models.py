from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField

def validate_image_size(value):
    limit_mb = 5
    if value.size > limit_mb * 1024 * 1024:
        raise ValidationError(_('Image size cannot exceed {limit} MB').format(limit=limit_mb))

class Listing(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=20)
    bedrooms = models.IntegerField(blank=True)
    bathrooms = models.IntegerField(default=2, blank=True)
    garage = models.IntegerField(default=2, blank=True)
    area = models.IntegerField(blank=True)
    lot_size = models.IntegerField(null=True, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', validators=[validate_image_size])
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_16 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_17 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_18 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    floor_plan = models.FileField(upload_to='floor_plans/%Y/%m/%d', blank=True, null=True)
    video = models.URLField(blank=True)
    home_open = models.CharField(max_length=200, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    sold = models.BooleanField(default=False)
    sold_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Listings"

    def __str__(self):
        return self.title

@receiver(post_save, sender=Listing)
def create_sold_listing(sender, instance, created, **kwargs):
    if instance.sold and not SoldListing.objects.filter(pk=instance.pk).exists():
        SoldListing.objects.create(
            title=instance.title,
            address=instance.address,
            description=instance.description,
            price=instance.price,
            bedrooms=instance.bedrooms,
            bathrooms=instance.bathrooms,
            garage=instance.garage,
            area=instance.area,
            lot_size=instance.lot_size,
            photo_main=instance.photo_main,
            photo_1=instance.photo_1,
            photo_2=instance.photo_2,
            photo_3=instance.photo_3,
            photo_4=instance.photo_4,
            photo_5=instance.photo_5,
            floor_plan=instance.floor_plan,
            video=instance.video,
            home_open=instance.home_open,
            is_published=instance.is_published,
            list_date=instance.list_date,
            sold_date=instance.sold_date or timezone.now()
        )

class SoldListing(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=20)
    bedrooms = models.IntegerField(blank=True)
    bathrooms = models.IntegerField(default=2, blank=True)
    garage = models.IntegerField(default=2, blank=True)
    area = models.IntegerField(null=True, blank=True)
    lot_size = models.IntegerField(null=True, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', validators=[validate_image_size])
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_16 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_17 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    photo_18 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, validators=[validate_image_size])
    floor_plan = models.FileField(upload_to='floor_plans/%Y/%m/%d', blank=True, null=True)
    video = models.URLField(blank=True)
    home_open = models.CharField(max_length=200, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    sold_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "Sold Listings"

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


class Feedback(models.Model):
    image = models.ImageField(upload_to='feedback_images/')
    review = models.TextField()
    author = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author