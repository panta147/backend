from django.urls import path
from . import views
urlpatterns = [
    path('companyList/', views.CompanyListAPIView.as_view(), name='company-list')
]