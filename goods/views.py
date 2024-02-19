from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Products


def catalog(request, category_slug, page=1):
    if category_slug == "all":
        goods = get_list_or_404(Products.objects.all())
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 4)
    current_page = paginator.page(page)

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, "goods/product.html", context)