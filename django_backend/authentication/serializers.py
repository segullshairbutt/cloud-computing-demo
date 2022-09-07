from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        return token


class UserRegistrationSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if attrs['email'][len(attrs['email']) - 12:] != '.hs-fulda.de':
            raise serializers.ValidationError({"error": "Should be a member of Fulda organization"})

        return attrs

    class Meta:
        model = User
        fields = 'id', 'email', 'first_name', 'last_name'
        extra_kwargs = {'password': {'write_only': True}}


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'email', 'first_name', 'last_name'


class UserUpdateSerializer(serializers.Serializer):
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class UserListingSerializerForChat(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'email', 'first_name', 'last_name'
