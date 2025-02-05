from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from banners.models import Banner
from banners.serializers import BannerSerializer
from products.models import Category, Brand
from products.serializers import CategorySerializer, BrandSerializer


# ---------- index page slider
# banner slider
@api_view(['GET'])
def get_banners(request):
    banners = Banner.objects.all().filter(is_active=True)
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data)


# category slider
@api_view(['GET'])
def get_category_slider(request):
    category_sliders = Category.objects.all().filter(is_in_slider=True)
    serializer = CategorySerializer(category_sliders, many=True)
    return Response(serializer.data)


# brand slider
@api_view(['GET'])
def get_brand_slider(request):
    brand_slider = Brand.objects.all().filter(is_in_slider=True)
    serializer = BrandSerializer(brand_slider, many=True)
    return Response(serializer.data)
