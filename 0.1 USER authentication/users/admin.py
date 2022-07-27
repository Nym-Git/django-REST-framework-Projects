from atexit import register
from django.contrib import admin
from .models import * 

admin.site.register(user_registration)
admin.site.register(otp_session)
