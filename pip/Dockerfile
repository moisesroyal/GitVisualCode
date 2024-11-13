FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /pip

# Copia el archivo de requisitos (o prueba.txt si es necesario)
COPY prueba.txt /pip/prueba.txt 

# Instala las dependencias desde el archivo de requisitos
RUN pip install --no-cache-dir --upgrade -r /pip/prueba.txt

# Copia todo el contenido del directorio actual al contenedor
COPY . /pip

# Mantén el contenedor corriendo, o ejecuta tu programa principal
CMD ["uvicorn", "main:pip", "--host", "0.0.0.0", "--port", "80"]
