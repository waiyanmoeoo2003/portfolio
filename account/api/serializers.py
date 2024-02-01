from django.contrib.auth import get_user_model
from account.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer, \
    TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims or data to the token payload if needed
        token['username'] = user.username
        token['prompt'] = "I luv you <3 ..."

        # Add more custom data as needed
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add additional data to the response if needed

        data['prompt'] = "I luv you <3 ..."
        # Add more custom data as needed
        print(data)
        return data

class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active')
        