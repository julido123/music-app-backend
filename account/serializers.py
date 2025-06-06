from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class LoginResponseSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    token = serializers.DictField() 