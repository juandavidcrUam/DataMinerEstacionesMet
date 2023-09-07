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

consulta_insert = "INSERT INTO climatologia_diaria.Organismo (id_organismo,nombre_org) VALUES (1,'CONAGUA-SMN'),(2,'CONAGUA-DGE');"
consulta_insert2="""
INSERT INTO climatologia_diaria.Estados_Republica_Mex (id_estado,nombre_estado) VALUES
     (1,'Aguascalientes'),
     (2, 'Baja California'),
     (3, 'Baja California Sur'),
     (4, 'Campeche'),
     (5, 'Coahuila de Zaragoza'),
     (6, 'Colima'),
     (7, 'Chiapas'),
     (8, 'Chihuahua'),
     (9, 'Distrito Federal'),
     (10, 'Durango'),
     (11, 'Guanajuato'),
     (12, 'Guerrero'),
     (13, 'Hidalgo'),
     (14, 'Jalisco'),
     (15, 'México'),
     (16, 'Michoacán de Ocampo'),
     (17, 'Morelos'),
     (18, 'Nayarit'),
     (19, 'Nuevo León'),
     (20, 'Oaxaca de Juárez'),
     (21, 'Puebla'),
     (22, 'Querétaro'),
     (23, 'Quintana Roo'),
     (24, 'San Luis Potosí'),
     (25, 'Sinaloa'),
     (26, 'Sonora'),
     (27, 'Tabasco'),
     (28, 'Tamaulipas'),
     (29, 'Tlaxcala'),
     (30, 'Veracruz de Ignacio de la Llave'),
     (31, 'Yucatán'),
     (32, 'Zacatecas');
"""
consulta_insert3 = """
INSERT INTO `Municipio` VALUES 
(1,30,'ATZALAN'),(2,30,'COATEPEC'),(3,30,'CHICONTEPEC'),(4,30,'COATEPEC 2'),(5,30,'CORDOBA'),
(6,30,'HUATUSCO'),(7,30,'SAN ANDRES TUXTLA'),(8,30,'SANTIAGO TUXTLA'),
(9,30,'SAN ANDRES TUXTLA 2'),(10,30,'SANTIAGO TUXTLA 2'),(11,30,'MISANTLA'),
(12,30,'PAPANTLA'),(13,30,'TEZONAPA'),(14,30,'TEZONAPA 2'),(15,30,'ZONGOLICA');
"""
cursor.execute(consulta_insert)
cursor.execute(consulta_insert2)
cursor.execute(consulta_insert3)
conexion.commit()
conexion.close()
