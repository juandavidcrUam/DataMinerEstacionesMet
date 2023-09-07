import mysql.connector

# Establece la conexión con la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)

# Crea un cursor para ejecutar consultas
cursor = conexion.cursor()

consulta_createBD = """
DROP DATABASE IF EXISTS climatologia_diaria;
CREATE DATABASE climatologia_diaria;
USE climatologia_diaria;
"""

cursor.execute(consulta_createBD)

hayBD=True
cursor.close()
conexion.close()
with open("creartablas.py", 'r') as archivopy:
        contenido_script = archivopy.read()
        # Ejecutar el contenido del script
        exec(contenido_script)
archivopy.close()