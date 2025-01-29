from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Tarea

# Create your tests here.

Usuario = get_user_model()

class PruebasTareas(APITestCase):
    #Pruebas unitarias para la API de tareas.

    def setUp(self):
        #Configuracion inicial antes de cada prueba.

        self.usuario = Usuario.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.usuario)
        self.tarea = Tarea.objects.create(owner=self.usuario, title="Tarea de prueba")

    def test_crear_tarea(self):
        #Verifica que se pueda crear una tarea correctamente.

        response = self.client.post('/api/tareas/', {'title': 'Nueva tarea'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_tareas(self):
        #Verifica que un usuario pueda listar sus tareas.
        
        response = self.client.get('/api/tareas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_tarea(self):
        #Verifica que un usuario pueda actualizar su tarea.
        
        response = self.client.put(f'/api/tareas/{self.tarea.id}/', {'title': 'Tarea Actualizada'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_eliminar_tarea(self):
        #Verifica que un usuario pueda eliminar su tarea.
        
        response = self.client.delete(f'/api/tareas/{self.tarea.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
