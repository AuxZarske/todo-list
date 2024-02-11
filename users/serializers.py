from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Definicion del Serializer para el modelo user,
    se especifican sus campos y se limita la vista del password.
    """
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
        """
        Se limita la actualizacion del campo email del usuario, siendo que este es su identificador.
        """
        if 'email' in validated_data:
            raise serializers.ValidationError("No puedes actualizar el campo 'email'.")

        instance.password = validated_data.get('password', instance.password)
        instance.save()

        return instance
