from rest_framework import serializers
from .models import *






class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 
    
class ProductReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductReview
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    Review = ProductReviewSerializer()
    class Meta:
        model = ecom_Products
        fields = '__all__'
 
 
