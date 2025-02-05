from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from banners.models import Banner
from banners.serializers import BannerSerializer
from products.models import Product, Category
from products.serializers import ProductSerializer


# filter, sort and get products
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    products = products.order_by('-id')

    # category filter
    category = request.GET.get('category')
    if category:
        find_category = Category.objects.filter(title_en=category)
        products = products.filter(category__in=find_category)

    # sort
    sort_param = request.GET.get('sort')
    if sort_param == 'price_asc':
        products = products.order_by('price_with_discount')
    elif sort_param == 'price_desc':
        products = products.order_by('-price_with_discount')
    elif sort_param == 'newer':
        products = products.order_by('-added_time')

    # home page hero slider
    hero_slider = request.GET.get('hero_slider')
    if hero_slider == 'true':
        products = Product.objects.all().filter(is_in_slider=True)
    elif hero_slider == 'false':
        products = Product.objects.all().filter(is_in_slider=False)

    count = request.GET.get('count')
    if count:
        products = products[:int(count)]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


