from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Product


def product_list(request):

    products = Product.objects.all()

    data = []

    for product in products:

        data.append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": float(product.price),
            "image": product.image.url if product.image else None
        })

    return JsonResponse(data, safe=False)


def product_detail(request, id):

    try:
        product = Product.objects.get(id=id)

    except Product.DoesNotExist:

        return JsonResponse(
            {
                "error": "Product not found"
            },
            status=404
        )

    data = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": float(product.price),
        "image": product.image.url if product.image else None
    }

    return JsonResponse(data)