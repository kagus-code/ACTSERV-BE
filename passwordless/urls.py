from django.urls import path,re_path,include
from . import views
urlpatterns = [

# User urls
path('users/register/', views.RegisterUserApiView.as_view(), name='register'),

]