from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} : {str(self.price)}'

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.menu_item.name}"
