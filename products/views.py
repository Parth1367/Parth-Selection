from django.shortcuts import render
from .models import Product


def shop(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request, "shop.html", context)