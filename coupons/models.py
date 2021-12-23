from django.db import models
from django.core.validators import MinValueValidator,  MaxValueValidator


# Create your models here.


class Coupon(models.Model):
    # code that users have to enter in order to appy the coupon to their purchase
    code = models.CharField(max_length=50, unique=True)
    # valid-from the datetime value that indicates when the coupon becomes valid
    valid_from = models.DateTimeField()
    # The datetime value that indicates which time the coupon becomes invalid
    valid_to = models.DateTimeField()
    # the discount rate to apply percentagewise
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    # active-a boolean that indicates whether the coupon is active
    active = models.BooleanField()


    def __str__(self):
        return self.code

