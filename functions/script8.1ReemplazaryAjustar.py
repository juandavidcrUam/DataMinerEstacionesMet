import mysql.connector
midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'
)
cursor=midb.cursor()
def reemplazar_caracter_ultimo_linea_anterior(nombre_archivo):
    with open(nombre_archivo, 'r+') as archivo:
        lineas = archivo.readlines()
        if len(lineas) >= 2:
            linea_anterior = lineas[-2].rstrip('\n')
            ultima_linea = lineas[-1].rstrip('\n')
            if len(linea_anterior) > 0:
                #linea_anterior = linea_anterior[:-1] + ''  
                linea_anterior = linea_anterior[:-2] + ';'  # Reemplazar el último caracter por un punto y coma
                lineas[-2] = linea_anterior + '\n'
                archivo.seek(0)
                archivo.writelines(lineas)
                archivo.truncate()

# Nombre del archivo
nombre_archivo = "Data.sql"

# Llamada a la función
reemplazar_caracter_ultimo_linea_anterior(nombre_archivo)

queryDeComprobacion = """
SELECT DISTINCT estacion_id,id_estacion,nombre_estacion,num_estacion,nombre_mun
FROM Datos_Climatologicos
LEFT JOIN Estacion_climatologica
ON Datos_Climatologicos.estacion_id = Estacion_climatologica.id_estacion
LEFT JOIN Municipio
ON Municipio.id_municipio=Estacion_climatologica.municipio_id;
"""
cursor.execute(queryDeComprobacion)
result=cursor.fetchall()
    #print(result)
for filaEstaciones in result:
        # latitud | longitud | altitud_msnm |
        print("| Estacion Id | Id Estacion |  Nombre | Número | Nombre Municipio |")
        print(filaEstaciones)
print("Revisa tu nuevo archivo Data.sql si deseas insetar de manera manual. Fin ")
