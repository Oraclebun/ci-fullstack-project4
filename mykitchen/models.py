from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from products.models import Product
import datetime
# Create your models here.

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Household(models.Model):
    """Class defining Household Object"""
    name = models.CharField(blank=False, max_length=50,
                            help_text='Household name')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='owner')
    member = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, blank=True, related_name='member')

    def __str__(self):
        return self.name


class Location(models.Model):
    """Location for items in a kitchen. E.g. Cabinet, Fridge"""
    name = models.CharField(blank=False, max_length=50, 
                            help_text="Kitchen Fixtures")
    storage_temperature = models.IntegerField(blank=True,
                                              help_text="Storage Temperatures in degC")
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    editted_by = models.ForeignKey(User, blank=False,
                                   on_delete=models.SET(get_sentinel_user))

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    """Food Items to be Stored in Location"""
    food = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    remarks = models.TextField(blank=True, max_length=600)
    expiry_date = models.DateField(blank=False)
    threshold = models.IntegerField(blank=False)
    edited_by = models.ForeignKey(User, blank=False,
                                   on_delete=models.SET(get_sentinel_user))

    PACKAGES = (
        ('bar', 'Bar'),
        ('bottle', 'Bottle'),
        ('box', 'Box'),
        ('pack', 'Pack'),
        ('roll', 'Roll'),
        ('tin', 'Tin')
    )

    package = models.CharField(blank=False, choices=PACKAGES,
                               max_length=7, default="pack",
                               help_text="Food Packages")

    def __str__(self):
        return f"{self.food} bought by {self.edited_by}"

    def get_food_name(self):
        return self.food.name

    def get_food_image(self):
        return self.food.image

    def get_food_brand(self):
        return self.food.brand

    def get_food_weight(self):
        return self.food.weight_per_pack

    def get_days_duration(self):
        return (self.expiry_date-datetime.date.today()).days

    def get_hit_threshold(self):
        return (self.expiry_date-datetime.date.today()).days <= threshold