from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])    

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True,unique = True)
    detail_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    minprice = models.DecimalField(max_digits=10, decimal_places=2)
    maxprice = models.DecimalField(max_digits=10, decimal_places=2)
    sale_address = models.CharField(max_length=200, db_index=True)
    youfei = models.CharField(max_length=200, db_index=True)
    beizhu = models.CharField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
   
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])
    
    def __str__(self):
        return self.name
    