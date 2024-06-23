from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('listings', views.listings, name='listings'),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('contact/', views.contact, name='contact'),
    path('sold', views.Sold, name='sold'),
    path('sold/<int:listing_id>/', views.sold_detail, name='sold_detail'),
    path('blogs/', views.blog_list, name='blogs'),
    #path('property/<int:pk>/', views.listing, name='listing'),
    # path('projects/', views.projects_view, name='projects'),
    # path('projects/<int:id>/', views.project_detail, name='project_detail'),
    # path('contact_form/', views.contact_view, name='contact_form'),
    # path('testimonials/', views.testimonial_list, name='testimonials'),
    # path('feedbackform', views.feedback_view, name='feedbackform'),
    
]