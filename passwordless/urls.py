from django.urls import path,re_path,include
from . import views
urlpatterns = [

# User urls
path('users/register/', views.RegisterApiView.as_view(), name='register'),
path('users/activate/<int:id>/',views.ActivateUserApiView.as_view(),name='activate-user'),
path('users/details/', views.UserDataApiView.as_view(), name="users-data"),


]