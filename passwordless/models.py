from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class User(AbstractUser):
	mobile=PhoneNumberField(unique=True,null=True)
	REQUIRED_FIELDS=[]