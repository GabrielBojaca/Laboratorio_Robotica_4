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
