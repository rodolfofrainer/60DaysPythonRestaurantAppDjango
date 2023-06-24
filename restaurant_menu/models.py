from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MEAL_TYPES = (
    ("Starters", "starters"),
    ("Salads", "salads"),
    ("Main Course", "main_course"),
    ("Desserts", "desserts"),
    ("Drinks", "drinks"),
)

class Item(models.Model):
    meal = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    meal_type = models.CharField(max_length=200,choices=MEAL_TYPES)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.meal