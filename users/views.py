from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.core.exceptions import BadRequest, ValidationError
#token generate imports
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.
from .models import User,Post
# from main.settings import *
from .serializers import *
import jwt
from main import settings
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import login,authenticate

#
import pytz
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives, send_mail
import base64
import random
import pyotp
import json



class LoginView(APIView):
    permission_classes=(AllowAny,)

    def post(self,request):
        if "email" in request.data and "password" in request.data:
            email=request.data['email']
            email=email.lower()
            password=request.data['password']
            try:
                user=User.objects.get(email=email) #agr email match krti h db vali email se.
            except User.DoesNotExist:
                return Response({"data": None,"message": "User Does Not Exist"},status = status.HTTP_400_BAD_REQUEST)
            
            if user.check_password(password): #check password if it matches.
                login(request, user)
                serializer=UserLoginSerializer(user)
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY) 
                user_details = serializer.data                   
                user_details["token"] = token
                  
                return Response({
                            "data": user_details,
                            "code": status.HTTP_200_OK,
                            "message": "Login SuccessFully",
                        },status = status.HTTP_200_OK)
            else:
                return Response({
                        "data": None,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "Invalid Credentials",
                        },status = status.HTTP_400_BAD_REQUEST)


from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver    

class RegisterView(APIView):
    permission_classes=(AllowAny,)

    def post(self,request):
        try:
            user=User.objects.get(email=request.data['email'])     
            return Response({"data":None,"message":"Email Already Exist"},status=status.HTTP_400_BAD_REQUEST) 
        except:
             
            otp = pyotp.random_base32()
            time_otp = pyotp.TOTP(otp, interval=300)
            otp = time_otp.now()
            Message = "Your One Time Passcode is {} to activate your account.".format(
                otp
            )
            from_email = settings.EMAIL_HOST_USER
            to_email = request.data["email"]

            # send_mail(
            #     "Email Varification<Don't Reply>",
            #     Message,
            #     from_email,
            #     [to_email],
            #     fail_silently=False,
            # )
            
            data=request.data.copy()
            data['email'] =request.data['email'].lower()
            data['otp']=otp
            # print(data)
            serializer=UserSignupSerializer(data=data)
            # print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

# def email_sender(sender,instance,**kwargs):


class Otp_Verification(APIView):
    permission_classes=[AllowAny,]
    def post(self,request):
        if "email" in request.data and "otp" in request.data:
            try:
                user = User.objects.get(email=request.data["email"].lower())
                if str(user.otp) == request.data["otp"]:
                    user.is_active = True
                    user.save()

                    return Response ({
                            "data": None,
                            "code": status.HTTP_200_OK,
                            "message": "Otp verification successfully",
                             },status = status.HTTP_200_OK)
                else:
                    return Response({
                        "data": None,
                        "code": status.HTTP_400_BAD_REQUEST,
                        "message": "You Entered Wrong OTP",
                    })

            except User.DoesNotExist:
                return Response({
                    "data": None,
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "User Does Not Exist",
                })
        else:
            return Response({
                "data": None,
                "code": status.HTTP_400_BAD_REQUEST,
                "message": "Please Enter All The Required Fields",
            })

class GetUserDetail(APIView):
    # permission_classes=[IsAuthenticated,]  
          
    def get(self,request):
        user = User.objects.get(id = request.user.id) 
        # print(request.user.id)   
        serializer = UserSignupSerializer(user)
        return Response(serializer.data,status = status.HTTP_200_OK)


class RegisterPost(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request):
        user = User.objects.get(id = request.user.id) 
        # print(user)
        post1=request.data.copy()
        # print(post1)
        post1['user'] = user.id   #user table ki id.
        # print(post1)
        
        serializer=PostSerializer(data=post1)
        if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
      
from django.db.models import Max,Count,Avg,Min
class PostView(APIView):
    # permission_class=[IsAuthenticated,]   
    def get(self,request):
        # user = Post.objects.get(id = request.user.id)
        # post=Post.objects.get(id=request.data['id'])  #behuuda loc.
        post=Post.objects.filter(user=request.user.id)  #return user and his post fields whose id is matches with request.user i.e bearer token
        post1= Post.objects.all().aggregate(Max('bedroom'))
        # post1=Post.objects.aggregate(Max('bedroom'),Min('bedroom'))
        # post1[0]
        print(post1)
        a=post.count()  
        print(a)
        # post=Post.objects.filter(user_id=request.user.id)  #same as upper line but (post) table ki (foreignkey) field (user_id) name se h but actual mai (user) table ki field (id) name se h.database ki fields kuch b naam ki ho skti h jb hum usey foreignkey assign krte h to hme apny python vali model fields ko priority deni hoti hai jo ki (id)  name se h.
        serializer=PostSerializer(post,many=True)
        return Response(serializer.data,    )

class RegisterPublication(APIView):
    permission_classes=[AllowAny,]
    def post(self,request):
        title=Publication.objects.get(title=request.data['title']) 
        title=request.data.copy()
        serializer=PublicationSerializer(data=title)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,statsu=statsu.HTTP_400_BAD_REQUEST)           





# class OtpGenerate(APIView):
#     permission_classes=[AllowAny,]
#     def post(self,request):
#         try:
#             # email=User.request.data['email']
#             user = User.objects.get(email=request.data['email'])
#             # user = User.objects.get(email=request.data['email'])
#         except User.DoesNotExist:
#             raise ValidationError(
#                 {
#                     "data": None,
#                     "code": status.HTTP_400_BAD_REQUEST,
#                     "message": "User Does Not Exist",
#                 }
#             )
#         if user:
#             otp = pyotp.random_base32()
#             time_otp = pyotp.TOTP(otp, interval=300)
#             otp = time_otp.now()
#             print(otp)
#             print(type(otp))
#             Message = "Your One Time Passcode is {} to activate your account.".format(
#                 otp
#             )
#             from_email = settings.EMAIL_HOST_USER
#             to_email = request.data["email"]
#             send_mail(
#                 "Email Varification<Don't Reply>",
#                 Message,
#                 from_email,
#                 [to_email],
#                 fail_silently=False,
#             )
#             serializer=OtpGenerateSerializer(user)
#             user_detail=serializer.data
#             user_detail['otp']=otp
#             # user_detail.otp=otp
#             # user_detail.save()  #throws a error.
            
#             user.otp = otp
#             user.save()
#             return Response(user_detail,status=status.HTTP_400_BAD_REQUEST)
#         return None
        


        
      








               




