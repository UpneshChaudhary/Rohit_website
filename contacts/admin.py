from django.contrib import admin
from django.shortcuts import render
from .models import Enquiry, MarketAppraisal



class EnquiryAdmin(admin.ModelAdmin):
    # ContactsAdmin configuration
    list_display = ('name', 'email', 'phone', 'listing')


admin.site.register(Enquiry, EnquiryAdmin)

class MarketAppraisalAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    list_filter = ['created_at']

admin.site.register(MarketAppraisal, MarketAppraisalAdmin)
