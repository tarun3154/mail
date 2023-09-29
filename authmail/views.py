from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import  EmailMessage
import os
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages

# Create your views here.

def Viewhome(request):
    mail = request.POST.get('mail')
    try:
        user = User.objects.get(email = mail)
        UserId =urlsafe_base64_encode(force_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        link = "http://127.0.0.1:8000/verify/"+UserId+'/'+token

        email = EmailMessage(subject='Verify Your Mail',
                             body='Verify Email Click Here' + link,
                             from_email=os.environ.get('EMAIL_USER'),
                             to=[mail])
        email.send()
        print(user)
    except:
        user = None

    
    
    

    print('mail',mail)
    return render(request,'index.html')


def verifyUser(request,userId,token):
    verification_success = True  
    # Example: Adding a success message
    messages.success(request, 'Email verification successful.')

    return render(request,'verify.html')
   
   

