from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'description', 'country')
        extra_kwargs = {
            'password': {'write_only': True}
            }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        
        if 'email' in validated_data:
            raise serializers.ValidationError("No puedes actualizar el campo 'email'.")

        # Lógica de actualización estándar para otros campos
        instance.bio = validated_data.get('bio', instance.bio)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        return instance
