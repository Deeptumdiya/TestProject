from .models import StudentProfile
from django.contrib.auth import login
from .serializers import UserRegisterSerializer,UserSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
# import pdb; pdb.set_trace()


# Register API
from django.core.mail import EmailMessage
class RegisterAPI(APIView):
    serializer_class = UserRegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            print(token)
            # current_site = get_current_site(request).domain
            # relativelink = reverse('email-verify')
            # absurls = 'http://'+current_site+relativelink+"?token="+str(token)
            # email_body = 'Hi ' + user.username + 'Use link to verify your email/n'+ absurls
            # data = {'email_body':email_body,'to_email':user.email,'email_Subject':'verify your Email'}
            # Util.sendemail(data)
            email = EmailMessage(subject="test", body=str(token), to=("deeptumdiya666@gmail.com",))
            email.send()
        else:
            return Response({'error':serializer.errors})

        return Response({'msg': 'User Created Success'})

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = StudentProfile.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    # def put(self, request, pk=None):
    #     id = pk
    #     user = UserRegister.objects.get(id=id)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Data Updated Success'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, pk=None):
    #     id = pk
    #     user = UserRegister.objects.get(id=id)
    #     serializer = UserSerializer(user, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Partial Updated Success'})
    #     return Response(serializer.errors)

    # def delete(self, request, pk=None):
    #     id = pk
    #     user = UserRegister.objects.get(id=id)
    #     user.delete()
    #     return Response({'msg': 'User Deleted Success'})


# class LoginAPI(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             #return the token
#             print(e)
#         return Response({'msg':'User Login Success'})


# class UserData(viewsets.ViewSet):
#     """To Get The Memebers Details"""

#     def list(self, request):
#         query = StudentProfile.objects.all()
#         # To get All Objects From the models and store in query object

#         serializers = UserRegisterSerializer(query, many=True)
#         # To serialize the objects data and return to the request server
#         return Response({'Users-List': serializers.data})
