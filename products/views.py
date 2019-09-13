from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product
from .forms import ProductsForm


def get_products(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'products.html' template
    """
    products = Product.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "products.html", {'products': products})


def product_detail(request, pk):
    """
    Create a view that returns a single
    Productt object based on the post ID (pk) and
    render it to the 'productdetail.html' template.
    Or return a 404 error if the product is
    not found
    """
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    return render(request, "productdetail.html", {'product': product})


def create_or_edit_product(request, pk=None):
    """
    Create a view that allows us to create
    or edit a product depending if the Post ID
    is null or not
    """
    product = get_object_or_404(Product, pk=pk) if pk else None
    if request.method == "PRODUCT":
        form = ProductsForm(request.PRODUCT, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect(product_detail, product.pk)
    else:
        form = ProductsForm(instance=product)
    return render(request, 'productform.html', {'form': form})