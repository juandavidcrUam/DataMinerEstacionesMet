#!/usr/bin/env python
# decoding: utf-8
# Script que separa la información de los txt
from functions.script1DataCleanUp import getInfoDataTable,getInfoData
from infoBD import buscar_archivos
from pexpect import EOF
# hayEstaciones=False
#hayBD = False

print("Oprime Ctrl + C para salir en cualquier momento.")
print("----------------------------------------------------------------------------")
print(f"        Bienvenido al programa * UAM DataMinerEstacionesMet *")
print("----------------------------------------------------------------------------")
# if hayBD==False:
#     with open("./CreaBDyOrg.py", 'r') as archivopy:
#         contenido_script = archivopy.read()
#         exec(contenido_script)
print(f'Instrucciones: 1.- Cargar archivos de estaciones climatologicas dentro de la carpeta ------------> bancdata.\n Por cada carpeta contiene el nombre del municipio.')
print(f'2.- Cada archivo es el nombre de la estacion climatologica\n')
#print("O corriendo el comando python3 CreaBDyOrg.py")
print(f'3.- Introduce tu carpeta con los datos de cada municipio por favor.\n')
print("---------------ejecutar el update de estaciones lo esta tomando dinamicamente ------------------------")

print("------------> Ejemplo: ./bancdata")
carpeta_ingresada = input("Ingrese la ruta de la carpeta a procesar: ")
print("Si ya tienes algun dato previo evita duplicarlo dando solo Enter")
print("4.-El primer archivo nombrado por ti procesa la Tabla Estaciones_climatologicas.\nEl segundo archivo contendra los datos de cada estacion ingresados de manera ordenada separada por el token:\n--------------------------------------------------")
nombre_archivo = input("Ingrese el nombre del archivo a producir (sin extension *.txt) Ejemplo: estaciones-climatologicas \n>>>")
nombre_datos_archivo= input("Ingrese el nombre del archivo para depositar sus datos para el de MODELO CONAGUA actual (sin extension *.txt): ")
#almacenamiento de rutas 
listaData=buscar_archivos(carpeta_ingresada)
nArchivos=len(listaData)
listaOpciones=[]
for archivos in listaData:
    print("*",archivos)
    archivo1=getInfoDataTable(archivos,nombre_archivo)
    archivo2=getInfoData(archivos,nombre_datos_archivo)
listaOpciones.append(archivo1)
listaOpciones.append(archivo2)

print(f"\n*|--------------------------------------------------------------------------|*")
print(f"*| Se ingresan: {nArchivos} en la carpeta ./target/* archivos                                                ")
print(f"*| Se generaron los siguientes archivos: {archivo1}, {archivo2}    ")
print(f"*|--------------------------------------------------------------------------|*")
print(f"\nOpcion 1:Procesar el archivo: {listaOpciones[0]} -----> para Poblar tu tabla de EstacionesClimatologicas.\nEl cual Inserta datos de Estaciones climatologicas en la base de datos:climatologia_diaria.\n Si YA cuentas con tus estaciones climatológicas cargadas no es necesario oprimir el '1'.\n*\nOpcion 2: Procesar tus datos correspondiente al archivo {listaOpciones[1]} con el municipio id ingresado por usuario.\n")
opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    print(f"Has elegido la opción 1.\n Se leera el archivo ---------->{listaOpciones[0]} y finalizará el proceso. Es necesario volver a correr el programa. (Para que valides si ya tienes en tu base de datos la información) ")
    with open("./functions/script3DataAnalisys.py", 'r') as archivopy:
        contenido_script = archivopy.read()
        exec(contenido_script)
   
elif opcion == "2":
    print(f"Has elegido la opción 2.\n Se leera el archivo {listaOpciones[1]} y finalizará el proceso sino tienes estaciones Climatologicas previamente ingresadas")
    with open("./functions/script8InsertDataStation.py", 'r') as archivopy:
        contenido_script3 = archivopy.read()
        exec(contenido_script3)

else:
    print("Opción no válida. Debes elegir entre 1 y 2. Fin")
