from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import *
from .serializers import *
from rest_framework.decorators import  permission_classes
from django.http.response import Http404
from .email import send_activation_email

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
class RegisterApiView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            name = request.data['username']
            email =  request.data['email']
            user = User.objects.get(username=name)
            id = user.id
            send_activation_email(name,email,id)
            user_data = serializer.data
            response = {
                "data": {
                    "user": dict(user_data),
                    "status": "success",
                    "message": "user added successfully please check your email to activate your account",
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class ActivateUserApiView(APIView):
  # update user to a valid user
  def patch(self, request, id, format=None):
    user=User.objects.get(id=id)
    serializers=ActivateSerializer(user, request.data, partial=True)
    if serializers.is_valid(raise_exception=True):
      serializers.save(is_active=True)
      valid_user=serializers.data 
      response = {
                "data": {
                    "user": dict(valid_user),
                    "status": "success",
                    "message": "Your email has been successfully confirmed you can now log in",
                }
            }
      return Response(response, status=status.HTTP_200_OK)
    return Response(status.errors, status=status.HTTP_400_BAD_REQUEST)