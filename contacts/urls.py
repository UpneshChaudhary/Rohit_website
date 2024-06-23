from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('Enquiry/', csrf_exempt(views.contact), name='Enquiry'),
    #path('send_bulk_email/', csrf_exempt(views.send_bulk_email_view), name='send_bulk_email'),
]
