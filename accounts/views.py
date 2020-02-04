from django.shortcuts import render, redirect

def register(request):

    if request.method == 'POST':
        
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # paginator = Paginator(listings, 6)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)

    # context = {
    #     'listings' : paged_listings
    # }

    return render(request, 'accounts/register.html')
    # , context

def login(request):

    return render(request, 'accounts/login.html')

def logout(request):

    return redirect('index')

def dashboard(request):

    return render(request, 'accounts/dashboard.html')