
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import get_token_for_user





class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id',  'username', 'email', 'mobile']

    def create(self, validated_data):
          instance =self.Meta.model(**validated_data)
          instance.is_active=False
          instance.save()   
          return instance


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile','is_active', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class JWTAuthTokenSerializer(serializers.Serializer):
    access = serializers.CharField()

    def __init__(self, *args, **kwargs):
        user_id = kwargs['data']['payload']['user_id']
        self.user = User.objects.get(pk=user_id)
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        data = super().validate(attrs)
        token, _ = get_token_for_user(self.user)
        data['access'] = str(token)
        return data

class ActivateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['is_active']    


