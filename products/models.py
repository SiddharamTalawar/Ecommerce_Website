from django.db import models
from django.utils.text import slugify
from search.models import ProductManager
from django.contrib.auth.models import User



class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200 , blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args,**kwargs)

    
    def __str__(self):
        return self.category_name





class ecom_Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(default=0.0)
    description=models.TextField()
    discuont=models.FloatField(blank=True, null=True)
    image=models.ImageField(upload_to="Images/")
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=200, blank=True)


    objects = ProductManager()



    def __str__(self) -> str:
        return self.name

class ProductReview(models.Model):
    product = models.ForeignKey(ecom_Products, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)

