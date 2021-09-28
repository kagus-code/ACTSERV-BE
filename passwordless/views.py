from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import *
from .serializers import *
from rest_framework.decorators import  permission_classes
from django.http.response import Http404

# Create your views here.

class RegisterUserApiView(generics.CreateAPIView):
    serializer_class= UserSerializer
    def post(self, request, format=None):
        data = request.data

        try:
            user = User.objects.create(
                username=data['username'],
                email=data['email'],
                mobile = data['mobile']
            )
            serializers = UserSerializer(user, many=False)

            return Response(serializers.data)
        except:
            message = {'detail': 'user with that email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
