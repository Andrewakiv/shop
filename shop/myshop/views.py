from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    data = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, 'myshop/product/list.html', context=data)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    data = {
        'product': product
    }

    return render(request, 'myshop/product/detail.html', context=data)

