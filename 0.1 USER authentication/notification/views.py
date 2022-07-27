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
from users import models
import requests
import random
import uuid

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def phone_otp(request):
 if request.method == 'GET':
  phone_number = request.GET.get('phone_number')
  if phone_number is None:
   return Response({"message": "Please provide phone number"}, status=status.HTTP_400_BAD_REQUEST)
  try:
   user = models.user_registration.objects.filter(contact_number=phone_number)
   if not len(user) > 0:
    return Response({"message": "Phone number is not linked to any account"}, status=status.HTTP_400_BAD_REQUEST)
  except Exception as e:
   print(e)
   return Response({"message": "Phone number is not linked to any account.","error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

  try:
   user = models.user_registration.objects.get(contact_number=phone_number)
   print(user)
  except models.user_registration.DoesNotExist:
   return Response({"message": "Phone number is not linked to any account"}, status=status.HTTP_400_BAD_REQUEST)

  if user:
   try:
    phonerec = models.otp_session.objects.filter(phone=phone_number).order_by('-created_at').first()
    if (datetime.now().astimezone() - phonerec.created_at).total_seconds() < 30:
     return Response({"message": "Need to wait 30 sec before requesting another OTP"}, status=status.HTTP_400_BAD_REQUEST)
   except Exception as e:
    print(e)
    pass
   #For testing
   if phone_number == "9369841533":
    otp = 123456
   else:
    otp = random.randint(100000, 999999)
   session_id = str(uuid.uuid4())
   otpRecord = models.otp_session(
    phone=phone_number,
    otp=otp,
    session_id=session_id
   )
   otpRecord.save()

   url = f"https://ib0lkqmctk.execute-api.ap-south-1.amazonaws.com/dev/otp/?phone_number={phone_number}&otp={otp}"
   if phone_number >= "9876500000" and phone_number <= "9876500100":
    jsonData = ""
   else:
    data = requests.get(url)
    jsonData = data.json()
   return Response({"message": "otp sent", "session_id": session_id, "microservice_response": jsonData}, status=status.HTTP_200_OK)
 else:
  return Response({"message": "phone number is not linked to any account"}, status=status.HTTP_400_BAD_REQUEST)


