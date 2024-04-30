from rest_framework import serializers
from .models import Product,Category,ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True,read_only=True)
    class Meta:
        model=Product
        fields=['name','price','category','images']
        

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)
    class Meta:
        model=Category
        fields=['name','products']


