import random
from datetime import timedelta

from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import VerificationCode


@api_view(['GET'])
def generate_code(request):
    number = request.GET.get("number")
    code = str(random.randint(1000, 9999))
    print(number)
    VerificationCode.objects.create(number=number, code=code)
    return Response({'code': code, 'number': number})


@api_view(['GET'])
def verify_code(request):
    code = request.GET.get('code')
    number = request.GET.get('number')
    verify_model = VerificationCode.objects.filter(number=number).last()
    if verify_model.code == code:
        user = authenticate(request, username=number, password='sina1234')
        if user is not None:
            login(request, user)
            VerificationCode.delete(verify_model)
        else:
            profile = User.objects.create_user(username=number, password='sina1234', phone=number)
            profile.save()
            user = authenticate(request, username=number, password='sina1234')
            login(request, user)
            VerificationCode.delete(verify_model)
            return Response({'status': 'signed up'})
        if request.user.is_authenticated:
            return Response({"status": 'logged in'})
    return Response({'status': "wrong code", 'number': number})


# logout view
@api_view(['GET'])
def logout_user(request):
    logout(request)
    return Response({"status": 'logged out'})
