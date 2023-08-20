from rest_framework import serializers
from core import models


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["phone_number"]


class UserCheckCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["phone_number", "check_code"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["phone_number", "referral_link"]


class UserInviteKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["invite_key"]
