from rest_framework import serializers,generics,permissions,exceptions,viewsets
from django.contrib.auth.models import User
from .models import *
from rest_framework import viewsets

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('artist', 'album_title', 'genre', 'email')


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ('album', 'art_type', 'art_title', 'image', 'email')


 
