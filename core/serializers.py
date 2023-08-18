from rest_framework import serializers
from core import models


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["phone_number"]
