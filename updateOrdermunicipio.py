import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='psytranc3',
    database='climatologia_diaria',
    auth_plugin='mysql_native_password'

)
    

# Crea un cursor para ejecutar consultas
cursor = conexion.cursor()

# orden de lectura automatica por parte de python
# * ./bancdata/chicontepec/chicontepec-CHICONTEPEC.txt
# * ./bancdata/coatepec/coatepec-COATEPEC.txt
# * ./bancdata/los-tuxtlas/sihuapan-SAN ANDRES TUXTLA.txt
# * ./bancdata/los-tuxtlas/san-andres-SAN ANDRES TUXTLA2.txt
# * ./bancdata/los-tuxtlas/santiago-tuxtla-SANTIAGO TUXTLA.txt
# * ./bancdata/los-tuxtlas/tapalapa-SANTIAGO TUXTLA2.txt
# * ./bancdata/tezonapa/tezonapa-2-vistahermosa-TEZONAPA.txt
# * ./bancdata/tezonapa/tezonapa-1-morotzingo-TEZONAPA2.txt
# * ./bancdata/papantla/papantla-PAPANTLA.txt
# * ./bancdata/briones/briones-COATEPEC.txt
# * ./bancdata/atzalan/atzalan-ATZALAN.txt
# * ./bancdata/misantla/misantla-MISANTLA.txt
# * ./bancdata/zongolica/zongolica-ZONGOLICA.txt
# * ./bancdata/cordoba/cordoba-heroicacordoba-CORDOBA.txt
# * ./bancdata/huatusco/huatusco-huatuscodechicuellar-HUATUSCO.txt


consulta_update1="UPDATE Municipio SET nombre_mun = 'CHICONTEPEC' WHERE id_municipio = 1;"
consulta_update2="UPDATE Municipio SET nombre_mun = 'COATEPEC' WHERE id_municipio = 2;"
consulta_update3="UPDATE Municipio SET nombre_mun = 'SAN ANDRES TUXTLA' WHERE id_municipio = 3;"
consulta_update4="UPDATE Municipio SET nombre_mun = 'TEZONAPA ' WHERE id_municipio = 7;"
consulta_update5="UPDATE Municipio SET nombre_mun = 'SAN ANDRES TUXTLA 2' WHERE id_municipio = 4;"
consulta_update6="UPDATE Municipio SET nombre_mun = 'PAPANTLA' WHERE id_municipio = 9;"
consulta_update7="UPDATE Municipio SET nombre_mun = 'SANTIAGO TUXTLA ' WHERE id_municipio = 5;"
consulta_update8="UPDATE Municipio SET nombre_mun = 'TEZONAPA 2' WHERE id_municipio = 8;"
consulta_update9="UPDATE Municipio SET nombre_mun = 'SANTIAGO TUXTLA 2' WHERE id_municipio = 6;"
consulta_update10="UPDATE Municipio SET nombre_mun = 'COATEPEC' WHERE id_municipio = 10;"
consulta_update11="UPDATE Municipio SET nombre_mun = 'ATZALAN' WHERE id_municipio = 11;"
consulta_update12="UPDATE Municipio SET nombre_mun = 'MISANTLA' WHERE id_municipio = 12;"
consulta_update13="UPDATE Municipio SET nombre_mun = 'ZONGOLICA' WHERE id_municipio = 13;"
consulta_update14="UPDATE Municipio SET nombre_mun = 'CORDOBA' WHERE id_municipio = 14;"
consulta_update15="UPDATE Municipio SET nombre_mun = 'HUATUSCO' WHERE id_municipio = 15;"

cursor.execute(consulta_update1)
cursor.execute(consulta_update2)
cursor.execute(consulta_update3)
cursor.execute(consulta_update4)
cursor.execute(consulta_update5)
cursor.execute(consulta_update6)
cursor.execute(consulta_update7)
cursor.execute(consulta_update8)
cursor.execute(consulta_update9)
cursor.execute(consulta_update10)
cursor.execute(consulta_update11)
cursor.execute(consulta_update12)
cursor.execute(consulta_update13)
cursor.execute(consulta_update14)
cursor.execute(consulta_update15)

# Confirma los cambios en la base de datos
conexion.commit()

# Cierra el cursor y la conexión
cursor.close()
conexion.close()
