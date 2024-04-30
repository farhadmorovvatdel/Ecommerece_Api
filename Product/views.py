from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from rest_framework import generics
from rest_framework import viewsets
from.serializer import ProductSerializer,CategorySerializer
from .models import Product,Category


class ProductListAPIView(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class ProductDetailRetriveAPIView(generics.RetrieveAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()


class CategoryDetailRetriveAPIView(generics.RetrieveAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()