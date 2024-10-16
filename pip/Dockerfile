FROM python:3.8

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /pip

# Copia el archivo de requisitos (o prueba.txt si es necesario)
COPY prueba.txt /pip/prueba.txt 

# Instala las dependencias desde el archivo de requisitos
RUN pip install --no-cache-dir --upgrade -r /pip/prueba.txt

# Copia todo el contenido del directorio actual al contenedor
COPY . /pip/

# Mantén el contenedor corriendo, o ejecuta tu programa principal
CMD ["bash", "-c", "while true; do sleep 1; done"]
