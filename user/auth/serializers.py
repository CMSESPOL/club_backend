from user.validators import password_valid, username_valid
from rest_framework import serializers
from user.serializers import MemberSerializer
from rest_framework.authtoken.models import Token

class AuthUserSerializer(serializers.ModelSerializer):

    token = serializers.CharField(read_only=True, source='key')
    user = MemberSerializer(read_only=True)

    class Meta:
        model = Token
        fields = [
            'token',
            'user'
        ]

class UserCredentialsSerializer(serializers.Serializer):

    username = serializers.CharField(validators=[username_valid])
    password = serializers.CharField(validators=[password_valid])
