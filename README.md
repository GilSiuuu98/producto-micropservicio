## Enrique Gil Alcántara
# Microservicio de Productos (Django + DRF)

## Objetivo
API RESTful para gestionar productos (crear, leer, actualizar, eliminar).

## Requisitos
- Python 3.11+
- Docker & docker-compose
- Django 4.2+, Django REST Framework

## Estructura principal del proyecto
- `config/` - configuración general de Django
- `products/` - app con modelo `Producto`, serializers, views y tests
- `Dockerfile`, `docker-compose.yml` - para ejecutar el servicio en Docker
- `requirements.txt` - dependencias
- `manage.py` - comando principal de Django

## Instalación y ejecución local
Crear una carpeta
- mkdir producto-micropservicio

Dirigirnos a la carpeta

- cd producto-micropservicio

Crear ambiente virtual de trabajo

- python -m venv .venv

Para activar el entorno virtual en PowerShell necesitas ajustar la política de ejecución, ejecuta

- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Activar entorno virtual

- .\.venv\Scripts\Activate.ps1

Crear requerimientos

- echo "Django>=4.2
djangorestframework
drf-spectacular" > requirements.txt

- pip install -r requirements.txt

## Crear proyecto Django llamado `config` (configuración) y app `products`
django-admin startproject config .
python manage.py startapp products

## Inicializar repositorio
git init
echo "__pycache__/" >> .gitignore

# Crear migraciones para la base de datos y aplicarlas
- python manage.py makemigrations
- python manage.py migrate

## Iniciar servidor local

- python manage.py runserver

## Ejecutar prueba unitarias

- python manage.py test

## API disponible en
http://localhost:8000/api/productos/

La documentación Swagger UI en:
http://localhost:8000/api/schema/swagger-ui/

## Como ejecutar (con Docker)
1. Construir y levantar:

- docker-compose up --build

## Ejecutar migraciones con docker

- docker-compose run web python manage.py migrate

## Crear super usuario, si es que se necsita

- docker-compose run web python manage.py createsuperuser

## Correr pruebass con docker

- docker-compose run web python manage.py test

## Endpoints esperados
- `GET /api/productos/` → Listar productos
- `POST /api/productos/` → Crear producto
- `GET /api/productos/{id}/` → Obtener producto
- `PUT /api/productos/{id}/` → Actualizar producto
- `DELETE /api/productos/{id}/` → Eliminar producto


## Método	Endpoint	          Descripción	                                    Ejemplo de uso
GET	  /api/productos/	Lista todos los productos registrados.	              GET http://localhost:8000/api/productos/
POST	  /api/productos/	Crea un nuevo producto.	                             POST http://localhost:8000/api/productos/
GET	  /api/productos/{id}/	Obtiene los detalles de un producto específico.	GET http://localhost:8000/api/productos/1/
PUT	  /api/productos/{id}/	Actualiza los datos de un producto existente.	PUT http://localhost:8000/api/productos/1/
DELETE	/api/productos/{id}/	Elimina un producto por su ID.	                DELETE http://localhost:8000/api/productos/1/

## Notas
- La base de datos por defecto es SQLite ("db.sqlite3" en el proyecto).
- Se cambia "SECRET_KEY" y "DEBUG" a valores apropiados en producción.
