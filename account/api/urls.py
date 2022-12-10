from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('userdetails/', views.UserDetails.as_view(), name='userdetails'),
    path('send-otp/', views.CreateOtp.as_view(), name='CreateOtp'),
    path('password/chanage/', views.UserPasswordChange.as_view(),
         name='password-change'),
    path('password-forget/', views.PasswordForgetAPIView.as_view(),
         name='password-forget'),

]
