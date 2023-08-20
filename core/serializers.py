from rest_framework import serializers
from django.core.validators import MinLengthValidator

from core import models


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["phone_number"]


class UserCheckCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[MinLengthValidator(12)])
    check_code = serializers.CharField(validators=[MinLengthValidator(4)])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["phone_number", "referral_link"]


class UserInviteKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["referral_link"]
