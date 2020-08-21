from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_superuser', 'is_active', 'is_staff']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        write_only_fields = ('password',)
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': False},
            'email': {'required': True},
        }
    
    def create(self, validated_data):
        user = User(**validated_data)

        user.set_password(validated_data['password'])
        user.save()
        return user
