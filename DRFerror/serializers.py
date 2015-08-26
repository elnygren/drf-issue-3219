from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Startup

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class StartupSerializer(serializers.ModelSerializer):
	admin = UserSerializer()
	class Meta:
		model = Startup
