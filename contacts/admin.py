from django.contrib import admin
from django.shortcuts import render
from .models import Enquiry



class EnquiryAdmin(admin.ModelAdmin):
    # ContactsAdmin configuration
    list_display = ('name', 'email', 'phone', 'listing')


admin.site.register(Enquiry, EnquiryAdmin)
