from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StudentProfile
# from .models import UserRegister


# User Serializer
class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    mobile_phone = serializers.CharField()
    # password = serializers.CharField()

    def create(self, validated_data):
        profile_data = validated_data.pop('mobile_phone')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        StudentProfile.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


# Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRegister
#         fields = ('id', 'username', 'firstname',
#                   'lastname', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user = UserRegister.objects.create_user(
    #         validated_data['firstname'], validated_data['lastname'], validated_data['email'], validated_data['password'])
    #     user.save()
    #     return user


# Login Serializer
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

