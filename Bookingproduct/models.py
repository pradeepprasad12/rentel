from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    


    def __str__(self):
        return f"{self.product.name} ({self.start_date} - {self.end_date})"

    def save(self, *args, **kwargs):
        if self.pk is None:
            if Booking.objects.filter(product=self.product, start_date__lte=self.end_date, end_date__gte=self.start_date).exists():
                raise ValueError("Product already booked for this date range.")
        super().save(*args, **kwargs)
