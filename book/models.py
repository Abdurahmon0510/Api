from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    published_date = models.DateField(default=timezone.now)
    pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     class Meta:
         abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.title


class Group(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="groups", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, related_name="products", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
