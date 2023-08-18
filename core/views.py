import random
import string
import time

from django.contrib.auth.models import User as Django_user
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core import serializers
from core import models


def create_check_code():
    return str(random.randint(1000, 9999))


def create_invite_key():
    key = ""
    for i in range(3):
        key += random.choice(list(string.ascii_lowercase))
        key += random.choice(list(string.digits))
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
                django_user = Django_user.objects.create(username='some_username',
                                                        password='some_password')
                models.User.objects.create(
                    user=django_user,
                    phone_number=serializer.validated_data["phone_number"],
                    check_code=check_code,
                    invite_key=create_invite_key(),
                )

            time.sleep(2)

            return Response(
                {
                    "result": True,
                    "check_code": check_code
                }
            )
        return Response(data={"result": False}, status=status.HTTP_400_BAD_REQUEST)
