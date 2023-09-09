#!/bin/bash

# Verificar si el usuario es root
if [ "$EUID" -ne 0 ]; then
  echo "Este script debe ejecutarse como root."
  exit 1
fi
# Preguntar al usuario si desea reinstalar MySQL Server
read -p "¿Desea reinstalar MySQL Server? (s/n): " reinstall_mysql

if [ "$reinstall_mysql" == "s" ]; then
  # Reinstalar MySQL Server
  apt-get update
  apt-get remove --purge mysql-server mysql-client mysql-common
  apt-get autoremove -y
  apt-get install -y mysql-server
fi
# Preguntar al usuario si desea cambiar la contraseña de la base de datos
read -p "¿Desea cambiar la contraseña de la base de datos MySQL? (s/n): " change_password

if [ "$change_password" == "s" ]; then
  # Pedir al usuario una nueva contraseña para el usuario root de MySQL
  read -p "Ingrese la nueva contraseña para el usuario root de MySQL: " mysql_root_password

  # Cambiar la contraseña del usuario root de MySQL
  mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '$mysql_root_password';"

  # Mostrar un mensaje de confirmación
  echo "La contraseña del usuario root de MySQL se ha cambiado correctamente."
else
  echo "No se ha cambiado la contraseña de la base de datos MySQL."
fi



# Mostrar un mensaje de finalización
echo "Proceso completado."
