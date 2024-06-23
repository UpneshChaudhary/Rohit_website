from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing, SoldListing
from .models import Blog

def home(request):
    latest_listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]
    return render(request, 'index.html', {'latest_listings': latest_listings})


def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')


def listings(request):
    all_listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': all_listings})





def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    photos = [
        listing.photo_1, listing.photo_2, listing.photo_3, listing.photo_4, listing.photo_5,
        listing.photo_6, listing.photo_7, listing.photo_8, listing.photo_9, listing.photo_10,
        listing.photo_11, listing.photo_12, listing.photo_13, listing.photo_14, listing.photo_15,
        listing.photo_16, listing.photo_17, listing.photo_18
    ]
    # Filter out None photos
    photos = [photo for photo in photos if photo]
    return render(request, 'listing_detail.html', {'listing': listing, 'photos': photos})


def Sold(request):
    all_sold = SoldListing.objects.all()
    return render(request, 'sold.html', {'sold': all_sold})



def sold_detail(request, listing_id):
    sold = get_object_or_404(SoldListing, id=listing_id)
    photos = [
        sold.photo_1, sold.photo_2, sold.photo_3, sold.photo_4, sold.photo_5,
        sold.photo_6, sold.photo_7, sold.photo_8, sold.photo_9, sold.photo_10,
        sold.photo_11, sold.photo_12, sold.photo_13, sold.photo_14, sold.photo_15,
        sold.photo_16, sold.photo_17, sold.photo_18
    ]
    # Filter out None photos
    photos = [photo for photo in photos if photo]
    return render(request, 'sold_detail.html', {'sold': sold, 'photos': photos})





def blog_list(request):
    # Retrieve all blog posts
    blogs = Blog.objects.all().order_by('-created_at')
    
    # Paginate the blogs (3 blogs per page)
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Retrieve recent posts (e.g., the latest 5 posts)
    recent_posts = Blog.objects.all().order_by('-created_at')[:5]
    
    # Render the blog.html template with the blogs and recent_posts context
    return render(request, 'blog.html', {'page_obj': page_obj, 'recent_posts': recent_posts})