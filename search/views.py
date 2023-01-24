from django.shortcuts import render

from rest_framework import generics
from products.models import ecom_Products
from products.serializers import ProductSerializer



class SearchListView(generics.ListAPIView):
    queryset = ecom_Products.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)
        q = self.request.GET.get('q')
        results = ecom_Products.objects.none()
        if q is not None:
            results = qs.search(q)
            return results
