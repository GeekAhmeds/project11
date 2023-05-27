from django.shortcuts import render
#from django.contrib.auth.views import LoginView
#from rest_framework.views import APIView
#from rest_framework import status
#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Create your views here.

#class LoginAPIView(APIView):
    #def get(self, request, *args, **kwargs):
        #login_view = LoginView.as_view(template_name=None, redirect_authenticated_user=True)
        #response = login_view(request)
        #if response.status_code == 302:
           # return Response({'detail': 'Logged in successfully.'}, status=200)
        #else:
            #return Response({'detail': 'Invalid credentials.'}, status=401)


# @csrf_exempt
# @api_view(['GET'])
# def user_login(request):
#     if request.method != 'GET':
#         return HttpResponseNotAllowed(['GET'])
    
#     username = request.GET.get('username')
#     password = request.GET.get('password')
#     if not (username and password):
#         return HttpResponseBadRequest('Missing login credentials')
    
#     user = authenticate(request, username=username, password=password)
#     if user is None:
#         return HttpResponseBadRequest('Invalid login credentials')
    
#     login(request, user)
#     return HttpResponse('Logged in successfully')
        



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer