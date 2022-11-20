from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
class RegisterAPIView(APIView):
    def post(self,request):
        data=request.data
        print(request)
        return Response({"message":data,'status':'ok'})