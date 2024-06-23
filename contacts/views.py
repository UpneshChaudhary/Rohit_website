from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Enquiry
from pages.models import Listing

# Create your views here.
def contact(request):
    if request.method == 'POST':
        try:
            listing_id = request.POST.get('listing_id')
            listing = request.POST.get('listing')
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            # Save the enquiry
            enquiry = Enquiry.objects.create(
                listing=listing,
                listing_id=listing_id,
                name=name,
                email=email,
                phone=phone,
                message=message
            )

            # Send email and WhatsApp message
            # send_email_and_whatsapp(listing, name, email, phone, message)

            # Send automatic reply email
            # subject = 'Thank you for your enquiry'
            # message = f'Thank you for submitting an enquiry, {name}. Khush will be in touch soon. Please feel free to contact her directly on 0411 094 249. Have a nice day.'
            # sender_email = settings.EMAIL_HOST_USER
            # recipient_email = email
            # send_mail(subject, message, sender_email, [recipient_email])

            messages.success(request, 'Your request has been submitted. Our team will get back to you soon')
            return redirect('/listing/' + listing_id)
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return HttpResponse('Error processing the request')
    else:
        return HttpResponse('Invalid request')
