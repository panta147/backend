from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from job.models import CompanyType,JobType,JobProvider
from rest_framework import status
from .serializer import JobPostSErializer
import json
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


class JobTypeAPIView(APIView):
    def get(self,request):
        try:
            jobs=JobType.objects.all()
            company_list=[]
            for job in jobs:
                company_list.append({
                    'uuid':job.uuid,
                    'name':job.name,
                    'image':request.build_absolute_uri(job.image.url),
                    'count':JobProvider.objects.filter(jobtype__uuid=job.uuid).count()
                })
            return Response({"message":"success","data":company_list},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"error",'error':str(e)},status=status.HTTP_400_BAD_REQUEST)




class JobPostAPIView(APIView):
    def post(self,request):
        try:
            data=request.data
            if data:
                serializer=JobPostSErializer(data=data,context={"request": request})
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"job is successfully saved","data":serializer.data},status=status.HTTP_200_OK)
                return Response({"message":"error","error":serializer.errors},status=status.HTTP_200_OK)
            else:
                return Response({"message":"error","error":'All field required'},status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message":"error",'error':str(e)},status=status.HTTP_400_BAD_REQUEST)


class JobListAPIView(APIView):
    def get(self,request):
        try:
            job=JobProvider.objects.all().order_by('?')[:9]
            serializer=JobPostSErializer(job,many=True,context={"request": request})
            return Response({"message":"list of job","data":serializer.data},status=status.HTTP_200_OK)


        except Exception as e:
            return Response({"message":"error",'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
