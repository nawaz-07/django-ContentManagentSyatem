from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models



class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = "email"
    password = models.CharField(max_length=100, validators=[
    MinLengthValidator(limit_value=8, message="Password must be at least 8 characters long."),
    RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])', message="Password must contain at least 1 lowercase and 1 uppercase letter."),
])
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")])
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{6}$', message="Pincode must be 6 digits.")])
    is_admin = models.BooleanField(default=False)

class ContentItem(models.Model): 
    title = models.CharField(max_length=30,blank=False)
    body = models.TextField(max_length=300,blank=False)
    summary = models.TextField(max_length=300,blank=False)
    categories = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/', blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)






