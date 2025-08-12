# Imagen base de Python
FROM python:3.11-slim

# Evita archivos .pyc y buffering en logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Carpeta de trabajo en el contenedor
WORKDIR /code

# Copiar requirements y instalar dependencias
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar todo el código al contenedor
COPY . /code/

# Puerto expuesto
EXPOSE 8000

# Comando para migrar y ejecutar
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
