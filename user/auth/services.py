from user.auth.serializers import AuthUserSerializer, UserCredentialsSerializer
from user.models import Member
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from django.db.utils import IntegrityError


class AuthService:

    def get_user_by_credentials(self, data):
        serializer = UserCredentialsSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

        try:
            user = Member.objects.get(username=username)
        except Member.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                detail="Credenciales incorrectas.")
        if user.check_password(password):
            return user
        raise exceptions.AuthenticationFailed(
            detail="Credenciales incorrectas.")

    def generate_auth_token(self, member: Member):
        try:
            token, _ = Token.objects.get_or_create(user=member)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed()
        serializer = AuthUserSerializer(token)
        return serializer.data
