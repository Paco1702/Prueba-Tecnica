# Prueba-Tecnica

# API REST - Gestor de Tareas con Django y DRF

Proyecto de prueva tecnica para API RESTful que permite la gestión de tareas, creada con Django y Django REST Framework.

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/Paco1702/Prueba-Tecnica.git
cd Prueba-Tecnica

2. Crear y activar el entorno virtual

python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Mac/Linux


3. Instalar dependencias

pip install -r Dependencias_Prueba.txt


4. Aplicar migraciones

python manage.py migrate


5. Crear un superusuario

python manage.py createsuperuser
(Sigue las instrucciones en pantalla para crear un usuario administrador.)


6. Ejecutar el servidor

python manage.py runserver

Acceder a la API en:
http://127.0.0.1:8000/api/
http://127.0.0.1:8000/admin/ (dministrar usuarios y tareas)

Endpoints de la API (Cambiar "TOKEN_Obtenido_JWT" por lo obtenido posterior a "acces")

POST /api/token/ ---> Obtener un token JWT
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=admin&password=admin"

POST /api/token/refresh/ ---> Refrescar un token JWT

Usuarios
POST /api/usuarios/registrar/ ---> Registrar un usuario
GET /api/usuarios/perfil/ ---> Ver perfil del usuario autenticado

Tareas
GET /api/tareas/ ---> Listar todas las tareas
bash:
curl -X GET http://127.0.0.1:8000/api/tareas/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT>"

POST /api/tareas/ ---> Crear una nueva tarea
bash:
curl -X POST http://127.0.0.1:8000/api/tareas/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT>" -d "title=Primera Tarea"

PUT /api/tareas/<id>/ → Actualizar una tarea
bash
curl -X PUT http://127.0.0.1:8000/api/tareas/1/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT>" -d "title=Tarea Modificada"
DELETE /api/tareas/<id>/ → Eliminar una tarea
bash:
curl -X DELETE http://127.0.0.1:8000/api/tareas/1/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT}"


Pruebas Unitarias
Para ejecutar las pruebas unitarias en Django, usa el siguiente comando:

python manage.py test
Esto ejecutará las pruebas que validan la funcionalidad de la API.


Tecnologías Utilizadas
Django 3.2.25 - Framework de backend
Django REST Framework - Creación de APIs
SQLite - Base de datos
SimpleJWT - Autenticación con JWT
Python 3.8+ - Lenguaje de programación

Autores
Paco1702 - Desarrollador del proyecto