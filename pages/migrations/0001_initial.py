# Generated by Django 5.0.6 on 2024-06-10 09:28

import datetime
import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.CharField(max_length=20)),
                ('bedrooms', models.IntegerField(blank=True)),
                ('bathrooms', models.IntegerField(blank=True, default=2)),
                ('garage', models.IntegerField(blank=True, default=2)),
                ('Area', models.IntegerField(blank=True)),
                ('lot_size', models.IntegerField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_9', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_10', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_11', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_12', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_13', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_14', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_15', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_16', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_17', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('photo_18', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', validators=[pages.models.validate_image_size])),
                ('floor_plan', models.FileField(blank=True, null=True, upload_to='floor_plans/%Y/%m/%d')),
                ('video', models.URLField(blank=True)),
                ('home_open', models.CharField(blank=True, max_length=200)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
            ],
            options={
                'verbose_name_plural': 'Listing',
            },
        ),
    ]
