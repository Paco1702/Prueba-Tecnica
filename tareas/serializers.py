from rest_framework import serializers
from .models import Usuario, Tarea
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class UsuarioSerializer(serializers.ModelSerializer):
    #Registrar usuarios y obtener informacion.
    
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)

class TareaSerializer(serializers.ModelSerializer):
    #Tareas.
    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tarea
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El título debe tener al menos 3 caracteres.")
        return value
