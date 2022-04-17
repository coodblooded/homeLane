from multiprocessing.dummy import Condition
from django.db import models

# Create your models here.

class HouseData(models.Model):
    date = models.DateTimeField()
    price = models.FloatField()
    bedrooms = models.IntegerField()
    sqft_living = models.IntegerField()
    sqft_lot = models.IntegerField()
    floors = models.FloatField()
    waterfront = models.IntegerField()
    view = models.IntegerField()
    condition = models.IntegerField()
    sqft_above = models.IntegerField()
    sqft_basement = models.IntegerField()
    yr_built = models.IntegerField()
    yr_renovated = models.IntegerField()
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    statezip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)





    class Meta:
        indexes = [
            models.Index(fields=["price"], name="price_idx"),
            models.Index(fields=["sqft_living"], name="sqft_living_idx"),
            models.Index(fields=["yr_built"], name="yr_built_idx"),
            models.Index(fields=["yr_renovated"], name="yr_renovated_idx"),
            
        ]
        db_table = "house_data"

