# Telnet
  
Módulo para trabajar con el protocolo telnet  

*Read this in other languages: [English](Manual_Telnet.md), [Español](Manual_Telnet.es.md).*
  
![banner](imgs/Banner_telnet.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### configuración
  
Inicia configuración telnet
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Servidor|Dirección IP o nombre de dominio|test.ftp.com|
|Puerto|Puerto de conexión|0|
|Asignar resultado a variable|Nombre de variable donde se almacenará el resultado de la conexión|Variable|
|Usuario|Usuario de conexión|user@test.com|
|Contraseña|Contraseña de conexión|******|

### Leer información
  
Lee toda la información hasta el cierre de la conexión
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Guardar resultado en variable|Nombre de variable donde se guardará la información leída|Variable|

### Escribir
  
Escribe datos en el socket
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a escribir|Dato a escribir en el socket|ls|
