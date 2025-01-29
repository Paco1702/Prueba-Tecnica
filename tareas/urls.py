from django.urls import path
from .views import api_home, RegistroUsuarioView, PerfilUsuarioView, ListaCrearTareaView, DetalleTareaView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Ruta para api
    # #Muestra mensaje
    path('', api_home, name='api_home'),
    
    # Autenticacion con JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Usuarios, registro y muestra perfil del usuario autenticado
    path('usuarios/registrar/', RegistroUsuarioView.as_view(), name='registrar_usuario'),
    path('usuarios/perfil/', PerfilUsuarioView.as_view(), name='perfil_usuario'),

    # creacion de tareas y la visualizacion, actualizacion y eliminacion
    path('tareas/', ListaCrearTareaView.as_view(), name='lista_crear_tarea'),
    path('tareas/<int:pk>/', DetalleTareaView.as_view(), name='detalle_tarea'),
]
