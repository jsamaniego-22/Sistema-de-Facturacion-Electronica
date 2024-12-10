# Dockerfile para el Backend en Django

FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala dependencias del sistema necesarias para compilar psycopg2
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*
    
RUN pip install --no-cache-dir -r requirements.txt

# Instala las dependencias directamente, incluyendo psycopg2
RUN pip install --upgrade pip
RUN pip install django psycopg2-binary Pillow

# Copia el resto del proyecto
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
