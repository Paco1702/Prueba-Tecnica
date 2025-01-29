from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, permissions
from .models import Usuario, Tarea
from .serializers import UsuarioSerializer, TareaSerializer

# Nueva vista para /api/
def api_home(request):
    #Mostrar un mensaje en la raiz de la API.
    
    return JsonResponse({"mensaje": "API del Gestor de Tareas"})

class RegistroUsuarioView(generics.CreateAPIView):
    #Registrar nuevos usuarios.

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilUsuarioView(generics.RetrieveAPIView):
    #Obtener el perfil del usuario autenticado.
    
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class ListaCrearTareaView(generics.ListCreateAPIView):
    #Listar y crear tareas.
    
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarea.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetalleTareaView(generics.RetrieveUpdateDestroyAPIView):
    #Ver, actualizar o eliminar una tarea.
    
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tarea.objects.filter(owner=self.request.user)
