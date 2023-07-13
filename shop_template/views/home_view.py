from django.shortcuts import render
from category.models import Category

from product.models import Product, ReviewRating

# Create your views here.
def HomeView(request):

    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    proall = Product.objects.all().filter(is_available=True).order_by('created_date')[0:4]
    tv = Product.objects.filter(category_id=5)[0:4]
    comp = Product.objects.filter(category_id=3)[0:4]
    watch = Product.objects.filter(category_id=6)[0:4]
    cloth = Product.objects.filter(category_id=8)[0:4]

    top = Product.objects.filter(toprated=1)[0:4]
    best = Product.objects.filter(bestsellar=1)[0:4]
    onsale = Product.objects.filter(onsale=1)[0:4]

    category = Category.objects.all()
    context={
        'products': products,
        'reviews': reviews,
        'category':category,
        'pro':proall,
        'tv':tv,
        'comp':comp,
        'watch':watch,
        'cloth':cloth,
        'top':top,
        'best':best,
        'onsale':onsale

    }

    return render(request, "home/home_index.html", context)





