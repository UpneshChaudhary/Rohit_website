from django.contrib import admin
from django.db import models
from .models import Listing, SoldListing
from .models import Blog
from ckeditor.widgets import CKEditorWidget
from .models import Feedback

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'price', 'is_published', 'list_date', 'sold')
    list_filter = ('is_published', 'list_date', 'price', 'sold')
    search_fields = ('title', 'address', 'description')
    ordering = ('-list_date',)
    list_editable = ('is_published', 'sold')
    readonly_fields = ('list_date',)

    fieldsets = (
        (None, {
            'fields': ('title', 'address', 'description', 'price')
        }),
        ('Property Details', {
            'fields': ('bedrooms', 'bathrooms', 'garage', 'area') 
        }),
        ('Media', {
            'fields': ('photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'floor_plan', 'video', 'qr_code')
        }),
        ('Other Details', {
            'fields': ('home_open', 'is_published', 'list_date', 'sold', 'sold_date')
        }),
    )

admin.site.register(Listing, ListingAdmin)
admin.site.register(SoldListing)


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')

# Register the Blog model with the BlogAdmin
admin.site.register(Blog, BlogAdmin)

admin.site.register(Feedback)