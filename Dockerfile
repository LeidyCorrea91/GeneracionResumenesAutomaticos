FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Agrega la raíz del proyecto al PYTHONPATH
ENV PYTHONPATH=/app

# Copia el archivo de requerimientos
COPY requirements.txt .

# Actualiza pip a la última versión
RUN pip install --upgrade pip

# Instala las dependencias sin utilizar la caché
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto
COPY . .

# Comando por defecto (por ejemplo, ejecutar tests)
CMD ["pytest", "tests"]
