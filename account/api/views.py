from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterAPIView(APIView):
<<<<<<< HEAD
    def post(self,request):
        data=request.data
        # print(request)
        return Response({"message":'success','status':'ok','data':data})
=======
    def post(self, request):
        data = request.data
        # print(request)
        return Response({"message": data, 'status': 'ok', 'admin': "amritpanta"})
>>>>>>> 1249fc6cb2f6ee027ea2df683d809ab783d8a8a2
