# Generated by Django 5.0.6 on 2024-06-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
