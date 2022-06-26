from django.db import models

# Create your models here.
class user_reg(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    phone_number=models.BigIntegerField()
    password=models.CharField(max_length=20)


class product_details(models.Model):
    typ = (
        ('Stock Full','Stock Full'),
        ('Out of Stock','Out of Stock'),
        ('none','unverified')
        )

    product_name=models.CharField(max_length=20)
    product_rate=models.IntegerField()
    product_description=models.CharField(max_length=100)
    product_status=models.CharField(max_length=30,choices=typ,default='Stock Full')

