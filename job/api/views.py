from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from job.models import CompanyType
from rest_framework import status
class CompanyListAPIView(APIView):
    def get(self,request):
        try:
            companys=CompanyType.objects.all()
            company_list=[]
            for company in companys:
                company_list.append({
                    'uuid':company.uuid,
                    'name':company.name
                })
            return Response({"message":"success","data":company_list},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"error"},status=status.HTTP_400_BAD_REQUEST)
