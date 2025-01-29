# Prueba-Tecnica

## API REST - Gestor de Tareas con Django y DRF

Proyecto de prueba técnica para API RESTful que permite la gestión de tareas, creada con Django y Django REST Framework.

---

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/Paco1702/Prueba-Tecnica.git
cd Prueba-Tecnica
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Mac/Linux
```

### 3. Instalar dependencias
```bash
pip install -r Dependencias_Prueba.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear un superusuario
```bash
python manage.py createsuperuser
```
(Sigue las instrucciones en pantalla para crear un usuario administrador.)

### 6. Ejecutar el servidor
```bash
python manage.py runserver
```

Acceder a la API en:
- [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## **Endpoints de la API**

🔹 **Importante:**  
Para los endpoints protegidos, **reemplazar `<TOKEN_Obtenido_JWT>`** por el token recibido en `POST /api/token/`.

### **Autenticación**
- **Obtener un token JWT**
```bash
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=admin&password=admin"
```
- **Refrescar un token JWT**
```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ -d "refresh=<TOKEN_REFRESH>"
```

### **Usuarios**
- **Registrar un usuario**
```bash
curl -X POST http://127.0.0.1:8000/api/usuarios/registrar/ -d "username=usuario&password=clave"
```
- **Ver perfil del usuario autenticado**
```bash
curl -X GET http://127.0.0.1:8000/api/usuarios/perfil/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT>"
```

### **Tareas**
- **Listar todas las tareas**
```bash
curl -X GET http://127.0.0.1:8000/api/tareas/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT>"
```
- **Crear una nueva tarea**
```bash
curl -X POST http://127.0.0.1:8000/api/tareas/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT>" -d "title=Primera Tarea"
```
- **Actualizar una tarea**
```bash
curl -X PUT http://127.0.0.1:8000/api/tareas/1/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT>" -d "title=Tarea Modificada"
```
- **Eliminar una tarea**
```bash
curl -X DELETE http://127.0.0.1:8000/api/tareas/1/ -H "Authorization: Bearer <TOKEN_Obtenido_JWT>"
```

---

## **Pruebas Unitarias**
Para ejecutar las pruebas unitarias en Django, usa el siguiente comando:
```bash
python manage.py test
```
Esto ejecutará las pruebas que validan la funcionalidad de la API.

---

## **Tecnologías Utilizadas**
- **Django 3.2.25** - Framework de backend
- **Django REST Framework** - Creación de APIs
- **SQLite** - Base de datos
- **SimpleJWT** - Autenticación con JWT
- **Python 3.8+** - Lenguaje de programación

---

## **Autor**
- **Paco1702** - Desarrollador del proyecto
