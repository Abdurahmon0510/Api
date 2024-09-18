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
