import mysql.connector

# Establece la conexión con la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)

consuta_createOrg="""
CREATE TABLE Organismo(
    id_organismo int(10) NOT NULL AUTO_INCREMENT,
    nombre_org varchar(255),
    PRIMARY KEY (id_organismo)
);
"""
consulta2_create = """
CREATE TABLE Estados_Republica_Mex(
id_estado int(5) NOT NULL AUTO_INCREMENT,
nombre_estado varchar(255),
PRIMARY KEY (id_estado)
);
"""

consulta3_create = """

CREATE TABLE Municipio(
    id_municipio int(10) NOT NULL AUTO_INCREMENT,
    estado_id int(5),
    nombre_mun varchar(255),
    PRIMARY KEY (id_municipio),
    FOREIGN KEY (estado_id) REFERENCES Estados_Republica_Mex(id_estado)
);

"""
consulta4_create="""
CREATE TABLE Estacion_climatologica (
    id_estacion int(20) NOT NULL AUTO_INCREMENT ,
    num_estacion varchar(50),
    nombre_estacion varchar(255),
    situacion varchar(255),
    municipio_id int(10),
    organismo_id int(10),
    latitud varchar(50),
    longitud varchar(50),
    altitud_msnm varchar(50),
    emision_fecha DATE,
    PRIMARY KEY (id_estacion),
    FOREIGN KEY (municipio_id) REFERENCES Municipio(id_municipio),
    FOREIGN KEY (organismo_id) REFERENCES Organismo(id_organismo)
);

"""
consulta5_create = """
CREATE TABLE Datos_Climatologicos(
     id_climatologicos int(10) NOT NULL AUTO_INCREMENT,
     fecha DATE,
     precipitacion_mm FLOAT(5,1),
     evaporacion_mm FLOAT(5,1),
     tmax FLOAT(3,1),
     tmin FLOAT(3,1),
     humedad_relativa FLOAT(4,2),
     estacion_id int(20),
     PRIMARY KEY (id_climatologicos),
     FOREIGN KEY (estacion_id) REFERENCES Estacion_climatologica(id_estacion)
 );   
"""

cursor = conexion.cursor()
cursor.execute(consuta_createOrg)
cursor.execute(consulta2_create)
cursor.execute(consulta3_create)
cursor.execute(consulta4_create)
cursor.execute(consulta5_create)
cursor.close()
conexion.close()
with open("poblarBD.py", 'r') as archivopy:
        contenido_script = archivopy.read()
        # Ejecutar el contenido del script
        exec(contenido_script)









