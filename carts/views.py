from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self , request):
        user = request.user
        cart = Cart.objects.get(user=user,ordered=False)
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializer(queryset, many=True).data
        return Response({"permission":"working"})


    def post(self , request):
        data = request.data
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user,ordered=False)
        Products =ecom_Products.objects.get(id = data.get('Products'))
        price = ecom_Products.price
        quantity = data.get('quantity')
        cart_items = CartItems(cart=cart,user=user,Products=Products,price=price,quantity=quantity)
        cart_items.save()
        
           
        cart_items = CartItems.objects.filter(user=user, cart=cart.id)
        for items in cart_items:
           cart.total_price += items.price
        cart.save() 
        return Response({'sucess':'items sucessfully adedd to your cart'})



    
    def update(self , request):
        data = request.data
        cart_items = CartItems.objects.get(id=data.get['id'])
        quantity = data.get['quantity']
        cart_items.quantity += quantity 
        cart_items.save()
        return Response({'sucess':'items sucessfully updated'})


    
    def delete(self , request):
        data = request.data
        cart_items = CartItems.objects.get(id=data.get['id'])
        cart_items.delete()
        user = request.user
        cart = Cart.objects.get(user=user)
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializer(queryset, many=True)
        return Response(serializer.data)


        