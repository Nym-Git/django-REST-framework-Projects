from asyncio import streams
import os
import smtplib
from email.message import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.email_service import send_mail


@csrf_exempt
@api_view(['POST'])
def parameter(request): 
    if request.method == 'POST':
        to_email= request.data.get('to_email')
        subject = request.data.get('subject')
        body = request.data.get('body')
        send_mail(to_email,subject,body)
        return Response({"success":"email has sent"})
