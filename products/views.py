from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()

    # فیلتر دسته‌بندی
    category = request.GET.get('category')
    if category:
        products = products.filter(category__name=category)

    # مرتب‌سازی
    sort_param = request.GET.get('sort')
    if sort_param == 'price_asc':
        products = products.order_by('price_without_discount')
    elif sort_param == 'price_desc':
        products = products.order_by('-price_without_discount')
    elif sort_param == 'popular':
        products = products.order_by('-quantity')

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
