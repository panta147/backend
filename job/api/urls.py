from django.urls import path
from . import views
urlpatterns = [
    path('companyList/', views.CompanyListAPIView.as_view(), name='company-list'),
    path('jobType/', views.JobTypeAPIView.as_view(), name='job-type'),
    path('postJob/', views.JobPostAPIView.as_view(), name='job-post'),
    path('jobList/', views.JobListAPIView.as_view(), name='job-list'),
]