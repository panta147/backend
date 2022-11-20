from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import MyUser as User
from rest_framework import status
from django.contrib.auth import authenticate,login

class RegisterAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            check_user_already_exist = User.objects.filter(email=data['email'])

            if check_user_already_exist:
                return Response({'message': 'User with Email already exist'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(email=data['email'],
                                            password=data['password'],
                                            first_name=data['name'],
                                            date=data['date'],
                                            address=data['address'],
                                            phone=data['phone'],
                                            companyName=data.get('companyName','null'),
                                            companyType=data.get('companyType','null'),
                                            userType =data['userType'],
                                            )
            user.save()
            response = {
                "status":"1",
                "message": "Register successfully.",
                "userType":user.userType
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':'0',"message":"error",'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        try:
            email = request.data["email"]
            password = request.data['password']
        except Exception:
            return Response({"message": "Enter Email and password"}, status=400)

        test = User.objects.filter(email=email).first()

        if test is None:
            return Response({'message': 'User Not Found.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)
        if user:
            response = {
                     "status":'1',
                          "message": "loggedIn successfully.",
                "data":
                    {
    
                        "uuid": user.uuid,
                        "name":user.first_name,
                        'userType':user.userType

                    },
           
            }
            return Response(response, status=200)
        else:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

  
