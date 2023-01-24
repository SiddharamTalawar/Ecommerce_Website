from django.shortcuts import render

from .serializers import *
from .models import *
# Create your views here.

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

   

class ProductView(generics.ListCreateAPIView):
    queryset = ecom_Products.objects.all()
    serializer_class = ProductSerializer
    
    def get(self,request,*args,**kwargs):
      return self.list(request,*args,**kwargs)
        
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        price= serializer.validated_data.get('price')
        description = serializer.validated_data.get('description')
        image= serializer.validated_data.get('image')
        serializer.save(name=name,price=price,description=description,image=image)

        

class ProductReviewview(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    
    def perform_create(self, serializer):
        content = serializer.validated_data.get('content')
        stars = serializer.validated_data.get('stars')
        serializer.save(content=content,stars=stars)
