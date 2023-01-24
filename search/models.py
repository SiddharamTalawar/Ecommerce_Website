from django.db import models
from django.db.models import Q



class ProductQuerset(models.QuerySet):
    def search(self,query):
        lookup = Q(name__icontains = query) | Q(description__icontains = query)
        qs = self.filter(lookup)
        return qs


class ProductManager(models.Manager):
    def get_queryset(self,*args,**kwargs): 
        return ProductQuerset(self.model, using=self._db)

    def search(self,query):
        return self.get_queryset().search(query)