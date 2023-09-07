--- datos climatologicos de los municipios insertados
SELECT DISTINCT estacion_id,id_estacion,nombre_estacion,num_estacion,nombre_mun
FROM Datos_Climatologicos
LEFT JOIN Estacion_climatologica
ON Datos_Climatologicos.estacion_id = Estacion_climatologica.id_estacion
LEFT JOIN Municipio
ON Municipio.id_municipio=Estacion_climatologica.municipio_id;

--- Indica cuantas estaciones unicas estan en la tabla de datos
SELECT distinct estacion_id FROM climatologia_diaria.Datos_Climatologicos ;

--- Informacion general de los datos incorporados 
(SELECT 
    fecha,
    tmax,tmin,
    precipitacion_mm,nombre_mun,
    nombre_org,nombre_estacion,
    latitud,longitud,
    altitud_msnm,emision_fecha,
    nombre_estado
FROM Datos_Climatologicos
LEFT JOIN Estacion_climatologica
ON Datos_Climatologicos.estacion_id = Estacion_climatologica.id_estacion
LEFT JOIN Municipio 
ON Estacion_climatologica.municipio_id = Municipio.id_municipio
LEFT JOIN Organismo
ON Estacion_climatologica.organismo_id = Organismo.id_organismo
LEFT JOIN Estados_Republica_Mex
ON Municipio.estado_id = Estados_Republica_Mex.id_estado);


--- filtra por id de estacion de Datos_climatologicos
SELECT 
fecha,tmax,tmin,precipitacion_mm,nombre_mun,nombre_org,nombre_estacion,latitud,longitud,altitud_msnm,emision_fecha,nombre_estado
FROM Datos_Climatologicos
LEFT JOIN Estacion_climatologica
ON Datos_Climatologicos.estacion_id = Estacion_climatologica.id_estacion
LEFT JOIN Municipio 
ON Estacion_climatologica.municipio_id = Municipio.id_municipio
LEFT JOIN Organismo
ON Estacion_climatologica.organismo_id = Organismo.id_organismo
LEFT JOIN Estados_Republica_Mex
ON Municipio.estado_id = Estados_Republica_Mex.id_estado where Datos_Climatologicos.estacion_id=1;


