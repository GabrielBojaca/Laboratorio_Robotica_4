# Laboratorio_Robotica_4

El archivo launch_turtle.sh permite ejecutar el nodo de turtlesim y el controlador de forma sencilla, basta con agregarle permisos de ejecución y ejecutarlo desde 
una terminal.

### Dar permisos de ejecución al script

Antes de poder ejecutar el archivo, es necesario darle permisos de ejecución.  
Esto solo debe hacerse una vez.

1. Abre una terminal.
2. Navegue hasta la carpeta donde está tu script. Ejemplo:

   ```bash
   cd /ruta/donde/esta/el/script
    ```

3. Otorgue permisos de ejecución con:

   ```bash
   chmod +x launch_turtle.sh
   ```
Después de este paso, el archivo ya puede ejecutarse como un programa normal.

### Ejecutar el script

Con los permisos configurados, ahora puede ejecutar el script desde la terminal.

1. Entre a la carpeta donde está el archivo:

   ```bash
   cd /ruta/donde/esta/el/script
   ```

2. Ejecuta el script:

   ```bash
   ./launch_turtle.sh
   ```

Al ejecutarlo:
- Se abrirá una terminal ejecutando `turtlesim_node`.
- Luego se abrirá otra terminal ejecutando tu nodo `move_turtle`.



# Aplicacion del lab en Linux usando ROS2 Humble
A continuacion se muestra el video donde se ve el codigo de pyhton creado funcionando en Ros2 Humble usando el turtlesim para el dibujo de cada una de las letras de los integrantes del equipo

Hacer click en la imagen o en el recuadro abajo de la imagen.
<p align="center">
  <a href="https://youtu.be/ppMkalenVMg">
    <img src="https://github.com/user-attachments/assets/250aeb39-6fe2-4911-bd64-38e69e73731d" 
         alt="Ver video de la práctica con robot Epson para paletizado." 
         width="450" />
  </a>


</p>

<p align="center">
  <a href="https://youtu.be/ppMkalenVMg">
    <img src="https://img.shields.io/badge/Ver%20en%20YouTube-%F0%9F%94%B4-red?style=for-the-badge" 
         alt="Ver en YouTube">
  </a>
</p>
