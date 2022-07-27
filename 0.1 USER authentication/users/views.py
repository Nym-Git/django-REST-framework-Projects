from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.decorators import user_passes_test
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.shortcuts import render
from datetime import datetime, date
from rest_framework import status
from .models import *
import requests
import random

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
  }

@permission_classes([AllowAny])
@api_view(['POST'])
def user_register(request):
  if request.method == 'POST':
    email = request.data.get('email')
    password = request.data.get('password')
    contact_number = request.data.get('contact_number')

    try:
      user = user_registration.objects.create_user(email=email, password=password, contact_number=contact_number, is_active=True)
      user.save()
      return Response({"message": "User registered successfully..."}, status=status.HTTP_201_CREATED)
    except Exception as e:
      print(e)
      return Response({"message": "something went wrong while registering", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def phone_otp(request):
#   if request.method == 'GET':
#     phone_number = request.GET.get('phone_number')
#     if phone_number is None:
#       return Response({"message": "Please provide phone number"}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#       user = user_registration.objects.filter(contact_number=phone_number)
#       if not len(user) > 0:
#         return Response({"message": "Phone number is not linked to any account"}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         print(e)
#         return Response({"message": "Phone number is not linked to any account.","error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#       user = user_registration.objects.get(contact_number=phone_number)
#       print(user)
#     except user_registration.DoesNotExist:
#       return Response({"message": "Phone number is not linked to any account"}, status=status.HTTP_400_BAD_REQUEST)

#     if user:
#       try:
#         phonerec = otp_session.objects.filter(phone=phone_number).order_by('-created_at').first()
#         if (datetime.now().astimezone() - phonerec.created_at).total_seconds() < 30:
#           return Response({"message": "Need to wait 30 sec before requesting another OTP"}, status=status.HTTP_400_BAD_REQUEST)
#       except Exception as e:
#         print(e)
#         pass
#       #For testing
#       if phone_number:
#         otp = 123456
#       else:
#         otp = random.randint(100000, 999999)
#       session_id = str(uuid.uuid4())
#       otpRecord = otp_session(
#         phone=phone_number,
#         otp=otp,
#         session_id=session_id
#       )
#       otpRecord.save()

#       # url = f"https://ib0lkqmctk.execute-api.ap-south-1.amazonaws.com/dev/otp/?phone_number={phone_number}&otp={otp}"
#       # if phone_number >= "9876500000" and phone_number <= "9876500100":
#       jsonData = ""
#       # else:
#       #   data = requests.get(url)
#       #   jsonData = data.json()
#       return Response({"message": "otp sent", "session_id": session_id, "microservice_response": jsonData}, status=status.HTTP_200_OK)
#     else:
#         return Response({"message": "phone number is not linked to any account"}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
@user_passes_test(lambda u: not u.is_authenticated)
def login(request):
  if request.method == 'POST':
  
    login_method = request.data.get("login_method")
    print("login_method: ",login_method)

    if login_method == "0":
      email = request.data.get("email")
      password = request.data.get("password")

      if email is None or password is None:
        return Response({'error': 'Please provide both email and password'},status=status.HTTP_400_BAD_REQUEST)
      try:
        user = user_registration.objects.get(email=email)

      except user_registration.DoesNotExist:
        return Response({'error': 'email Not Registered or Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)

      if check_password(password, user.password):
        token = get_tokens_for_user(user)
        return Response({"token": token, "email": user.email}, content_type="appliaction/json", status=status.HTTP_200_OK)
      else:
        return Response({"message": "password is not matching"}, status=status.HTTP_400_BAD_REQUEST)
      
    # OTP part
    elif login_method == "1":
      phone_number = request.data.get('contact_number')
      session_id = request.data.get('session_id')
      otp = request.data.get('otp')

      if phone_number is None:
        return Response({"message": "please provide phone numberyep"}, status=status.HTTP_400_BAD_REQUEST)
      
      if session_id is None:
        return Response({"message": "please provide session id"}, status=status.HTTP_400_BAD_REQUEST)
      
      if otp is None:
        return Response({"message": "please provide otp"}, status=status.HTTP_400_BAD_REQUEST)

      try:
        user = user_registration.objects.get(contact_number=phone_number)
      except:
        return Response({"message": "phone number does not exist"}, status=status.HTTP_404_NOT_FOUND)

      try:
        otpRecord = otp_session.objects.get(session_id=session_id)
      except:
        return Response({"message": "session id does not exist"}, status=status.HTTP_404_NOT_FOUND)
      # otp timeout 5 mins
      print(phone_number, type(phone_number))
      
      if otpRecord.phone != int(phone_number):
        return Response({"message": "Invalid phone no for this session."}, status=status.HTTP_404_NOT_FOUND)

      if (datetime.now().astimezone() - otpRecord.created_at).total_seconds() > 300:
        return Response({"message": "Session expired. Generate new OTP"}, status=status.HTTP_404_NOT_FOUND)
      
      if user or otpRecord:
        if otpRecord.otp == int(otp):
          token = get_tokens_for_user(user)
          print(user.userid)
          try:
            applicants = user_registration.objects.get(contact_number=user.contact_number)
          except user_registration.DoesNotExist:
            return Response({'error': 'User not found'},status=status.HTTP_404_NOT_FOUND)
          except Exception as e:
            return Response({'error': 'User not found.', 'e': str(e)},status=status.HTTP_404_NOT_FOUND)
          
          otpRecord.delete()
          try:
            otp_session.objects.filter(phone=phone_number).delete()
          except Exception as e:
            print(e)
            return Response({"message": "somthing went wrong"}, status=status.HTTP_400_BAD_REQUEST)

          return Response({"message": "otp verified", "token": token}, status=status.HTTP_200_OK)
        else:
          return Response({"message": "otp not verified"}, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({"message": "phone number is not linked to any account"}, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({"message": "required login_method 0-email 1-phone"}, status=status.HTTP_400_BAD_REQUEST)
