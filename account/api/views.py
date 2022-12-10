import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User, Otp
from rest_framework import status
from django.contrib.auth import authenticate
from .serializer import UserSerializer
import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class CreateOtp(APIView):
    def post(self, request):
        data = request.data
        otp = random.randint(1000, 9999)
        check = Otp.objects.filter(email=data['email'])
        if check:
            check.update(otp=otp)
        else:
            Otp.objects.create(email=data['email'], otp=otp)
        html_content = render_to_string("Email/Otp_email.html",
                                        {'title': 'Otp', 'contend': otp, 'email': data["email"]})
        test_contend = strip_tags(html_content)
        email = EmailMultiAlternatives('Otp for emailUserType verification', test_contend, settings.DEFAULT_FROM_EMAIL,
                                       [data['email']])
        email.attach_alternative(html_content, 'text/html')
        email.send()
        return Response({'message': 'Done'})


class RegisterAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            check_user_already_exist = User.objects.filter(
                email=data['email'])
            if check_user_already_exist:
                return Response({'message': 'User with Email already exist'}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(email=data['email'],
                                            password=data['password'],
                                            first_name=data['name'],
                                            date=data.get('date', 'null'),
                                            address=data['address'],
                                            phone=data['phone'],
                                            companyName=data.get(
                'companyName', 'null'),
                companyType=data.get(
                'companyType', 'null'),
                userType=data['userType'],
            )
            user.save()
            response = {
                "status": "1",
                "message": "Register successfully.",
                "userType": user.userType
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': '0', "message": "error", 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        try:
            email = request.data["email"]
            password = request.data['password']
        except Exception as e:
            return Response({"message": "Enter Email and password", 'error': str(e)}, status=400)
        test = User.objects.filter(email=email).first()

        if test is None:
            return Response({'message': 'User Not Found.'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(request, email=email, password=password)
        if user:
            response = {
                "status": '1',
                "message": "loggedIn successfully.",
                "data":
                    {

                        "uuid": user.uuid,
                        "name": user.first_name,
                        'userType': user.userType

                    },

            }
            return Response(response, status=200)
        else:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    def get(self, request):
        try:
            uuid = request.query_params.get('uuid', None)
            if uuid:
                user = User.objects.get(uuid=uuid)
                ser = UserSerializer(user, context={"request": request}).data
                return Response(ser, status=status.HTTP_200_OK)
            else:
                return Response("user uuid is need ")
        except Exception as e:
            return Response({"error": str(e)})


class UserPasswordChange(APIView):
    def post(self, request):
        try:
            data = request.data
            user = User.objects.get(uuid=data['uuid'])
            check_old_password = authenticate(
                email=user.email, password=data['old_password'])
            if check_old_password:
                if data['new_password'] == data['confirm_password']:
                    user.set_password(data['new_password'])
                    user.save()
                    return Response({'message': 'Password Updated successfully.', 'status': 1})
                else:
                    return Response({'message': 'confirm and new pass is not match', "status": 0}, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({'message': 'Old password not matched', "status": 0}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e), "status": 0}, status=status.HTTP_400_BAD_REQUEST)


class PasswordForgetAPIView(APIView):
    def post(self, request):
        data = request.data
        check_otp = Otp.objects.filter(email=data['email'], otp=data['otp'])
        if check_otp:
            try:
                user = User.objects.get(email=data['email'])
            except Exception:
                return Response({'message': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(data['new_password'])
            user.save()
            return Response({'message': 'Done'})
        else:
            return Response({'message': 'Otp is not matched'}, status=status.HTTP_400_BAD_REQUEST)
