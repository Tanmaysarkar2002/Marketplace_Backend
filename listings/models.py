from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import for timestamps

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE) 
    rating = models.IntegerField(choices=((1, "1 Star"), (2, "2 Stars"), (3, "3 Stars"), (4, "4 Stars"), (5, "5 Stars")))
    comment = models.TextField()

    