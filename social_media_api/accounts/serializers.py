from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError

User = get_user_model().objects.create_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "bio", "profile_picture")
        extra_kwargs = {
            'password': {'write_only': True}
        }

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "bio", "profile_picture")

        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data["username"],
                password=validated_data["password"],
                bio=validated_data.get("bio"),
                profile_picture=validated_data.get("profile_picture")
            )
            Token.objects.create(user=user)
            return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if user is None or not user.check_password(data["password"]):
            raise ValidationError("Invalid username or password.")
        return user