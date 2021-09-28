
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *





class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id',  'username', 'email', 'mobile']




