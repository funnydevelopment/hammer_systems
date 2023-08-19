import random
import string
import time

from django.contrib.auth.models import User as Django_user
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core import serializers
from core import models


def create_check_code() -> str:
    return str(random.randint(1000, 9999))


def create_invite_key() -> str:
    key = ""
    for i in range(3):
        key += random.choice(list(string.ascii_lowercase))
        key += random.choice(list(string.digits))
    key_is_exist = models.User.objects.filter(invite_key=key).exists()
    if key_is_exist:
        return create_invite_key()
    return key


class UserCreateAPI(APIView):
    # todo сделать проверку авторизации и не создавать пользователя если не подошел код
    @staticmethod
    def post(request):
        serializer = serializers.UserAuthSerializer(data=request.data)

        if serializer.is_valid():
            user = models.User.objects.filter(
                phone_number=serializer.validated_data["phone_number"]
            )

            check_code = create_check_code()

            if user.exists():
                needed_user = user.first()
                needed_user.check_code = check_code
                needed_user.save()
            else:
                django_user = Django_user.objects.create(
                    username=f"user {serializer.validated_data['phone_number']}"
                )
                django_user.set_unusable_password()
                django_user.save()
                models.User.objects.create(
                    user=django_user,
                    phone_number=serializer.validated_data["phone_number"],
                    check_code=check_code,
                    invite_key=create_invite_key(),
                )

            time.sleep(2)

            return Response(data={"result": True, "check_code": check_code})
        return Response(data={"result": False}, status=status.HTTP_400_BAD_REQUEST)


class UserCheckCodeAPI(APIView):
    @staticmethod
    def patch(request):
        serializer = serializers.UserCheckCodeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = models.User.objects.get(
                    phone_number=serializer.validated_data["phone_number"],
                    check_code=serializer.validated_data["check_code"],
                )
                token, _ = Token.objects.get_or_create(user=user.user)
                return Response(
                    data={
                        "check_code_status": True,
                        "auth_token": str(token),
                    }
                )
            except models.User.DoesNotExist:
                pass
        return Response(
            data={"check_code_status": False}, status=status.HTTP_400_BAD_REQUEST
        )


class UserProfileAPI(APIView):
    authentication_classes = [TokenAuthentication]

    @staticmethod
    def get(request):
        print(request.user.profile)
        return Response(data={"result": "ok"})

    @staticmethod
    def post(request):
        pass
