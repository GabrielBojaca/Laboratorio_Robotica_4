<p align="center">
  <img src="https://github.com/user-attachments/assets/dbd3fe7d-6ee8-4415-9bd6-35dfebacb376">
</p>

<!-- ✦✦✦ FUTURE IS AUTOMATED ✦✦✦ -->
<!-- Banner superior "neón" -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=250&width=100%&color=0:04041A,50:14213D,100:0A4D68&text=Laboratorio%204&fontColor=E0FBFC&fontSize=60&fontAlign=50&fontAlignY=25&desc=Introducción%20a%20ROS%202%20y%20Turtlesim&descSize=24&descAlign=50&descAlignY=55" alt="header" />
</p>

<h1 align="center">🤖 LABORATORIO 4 – INTRODUCCIÓN A ROS 2 HUMBLE - TURTLESIM</h1>

## Laboratorio 4: Introducción a ROS 2 y Turtlesim



<center>
<div style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/b25c60f2-1fe4-4063-85d4-3cb31e83c775" width="500" height="550" />
</div>
</center>





## Objetivos
- **Control manual** de la tortuga usando el teclado.
- **Dibujo automático** de letras personalizadas con el simulador Turtlesim.
- **Familiarización con los conceptos fundamentales de ROS 2**: nodos, tópicos, y servicios.

## Procedimiento

### 1. Instalación y configuración
1. **Lanzar el simulador de Turtlesim**:
   ```bash
   source /opt/ros/humble/setup.bash
   ros2 run turtlesim turtlesim_node
   ```
2. **Compilar y ejecutar el código Python**:
   ```bash
   source /opt/ros/humble/setup.bash
   cd ~/ros2_ws
   colcon build
   source install/setup.bash
   ros2 run my_turtle_controller move_turtle
   ```

### 2. Control manual

El control manual de la tortuga se realiza utilizando las **flechas del teclado**:
- Flecha **↑**: avanzar.
- Flecha **↓**: retroceder.
- Flecha **←**: girar a la izquierda.
- Flecha **→**: girar a la derecha.

### 3. Dibujo automático de letras

![Dibujo](https://github.com/user-attachments/assets/af28ae7c-344e-40e2-b337-cfbbed3c263a)


La tortuga dibuja las letras de las iniciales del equipo utilizando teclas específicas:
- **Tecla M**: dibuja la letra "M".
- **Tecla F**: dibuja la letra "F".
- **Tecla C**: dibuja la letra "C".

Además, las secuencias de palabras pueden ser dibujadas con las teclas:
- **'1'**: dibuja la secuencia **SABP**.
- **'2'**: dibuja la secuencia **SFRM**.
- **'3'**: dibuja **SABP + SFRM**.

### 4. Estructura del código

El código se encuentra organizado en varias funciones, donde cada una es responsable de tareas específicas:
- **move_turtle2.py**: Nodo principal que maneja el control de la tortuga y las secuencias de letras.
- **Funciones de movimiento**: `move_timed`, `rotate_to_angle`, y `go_to_point` permiten controlar el movimiento y la orientación de la tortuga con precisión.
- **Dibujo de letras**: Se implementan funciones para dibujar las letras de forma continua (`draw_S_continuous`, etc.).

### 5. Diagrama de flujo

El diagrama de flujo a continuación resume el funcionamiento principal del nodo:

```mermaid
---
config:
  theme: redux
---
flowchart TB
    n1(["Inicio"]) --> n2["Iniciar ROS2"]
    n2 --> n3["Crear nodo <br><code>TurtleWriter</code>"]
    n3 --> n4["Crear publicador de<br>velocidad <code>/turtle1/cmd_vel</code>"]
    n4 --> n5["Crear suscriptor de pose<br><code>/turtle1/pose</code>"]
    n5 --> n6["Crear clientes de servicios <br><code>teleport_absolute</code>, <code>set_pen</code>"]
    n6 --> n7["Esperar a recibir la primera <br>pose de la tortuga"]
    n7 --> n8["Mover tortuga a posición inicial"]
    
    %% Conexión al hilo de teclado (paralelo)
    n7 --- n15(["Bucle de lectura<br>teclado"])
    
    %% Flujo principal
    n8 --> n9["Inicializar variables de renglones y conteo de letras"]
    n9 --> n10["Crear y arrancar hilo de lectura de teclado"]
    n10 --> n11["Ejecutar bucle de ROS 2"]
    n11 --> n12{"¿Se solicita cierre ?"}
    n12 -- Sí --> n13["Destruir nodo y cerrar ROS 2"]
    n13 --> n14(["FIN"])
    n12 -- NO --> n7
    
    %% Hilo de Teclado
    n15 --> n16["Leer tecla del usuario (<code>get_key</code>)"]
    n16 --> n17["Convertir tecla a mayúscula"]
    n17 --> n18{"¿Nodo ocupado (<code>busy</code> = True)?"}
    n18 -- Si --> n19["Ignorar tecla / esperar siguiente tecla"]
    n18 -- NO --> n20{"¿Tecla es una letra válida (J, N, G, A, C, P, M, E, B)?"}
    n19 --> n18
    n20 -- NO --> n21["Ignorar tecla / volver a leer"]
    n20 -- Sí --> n22["Marcar nodo como ocupado (<code>busy = True</code>)"]
    n21 --> n16 
    
    %% Ejecución de Dibujo
    n22 --> n23["Mostrar mensaje: Dibujando [letra]..."]
    n23 --> n24["Llamar función de dibujo<br>draw_"]
    n24 --> n25(["Funcion draw_"])
    n25 --> n27["Marcar nodo como libre (<code>busy = False</code>)"]
    n27 --> n26["Mostrar mensaje: Letra [letra] lista."]
    n26 --> n16
    
    %% Subflujo de la Función draw_ (Dentro de 25)
    subgraph Proceso de Dibujo
        n25 --> n28["Guardar posición inicial de la letra"]
        n28 --> n29["Configurar pluma: levantar o bajar"]
        n29 --> n30["Ejecutar secuencia de movimientos lineales ( <code>move_line</code> )"]
        n30 --> n31["Ejecutar giros necesarios (<code>rotate</code>)"]
        n31 --> n32["Completar la forma de la letra"]
        n32 --> n33["Llamar a <code>finish_letter(...)</code>"]
    end
    
    %% Flujo de finish_letter (Subflujo de 33)
    subgraph Finalizar Letra
        n33 --> n36(["Funcion finish_letter"])
        n36 --> n34["Levantar pluma"]
        n34 --> n35["Incrementar contador de letras en la línea actual"]
        n35 --> n37{"¿Contador de letras ≥ 4?"}
    end
    
    %% Salto de Línea
    n37 -- SÍ --> n38["Mostrar mensaje “Salto de línea”"] 
    n38 --> n39["Reiniciar contador de letras a 0"]
    n39 --> n40["Incrementar número de renglón (<code>current_line += 1</code>)"]
    n40 --> n41["Calcular nueva posición de inicio de renglón"]
    n41 --> n44
    
    %% No Salto de Línea
    n37 -- NO --> n42["Calcular nueva posición en X para la siguiente letra"]
    n42 --> n43["Mantener la misma altura (<code>start_y</code>)"]
    n43 --> n44["Teletransportar tortuga a nueva posición de inicio de letra"]
    
    %% Continuación
    n44 --> n45["Bajar pluma de nuevo para la próxima letra"]
    n45 --> n25
    
    %% Estilos (Solo para asegurar formas y bordes, sin forzar el color de fondo)
    style n12 shape:diamond
    style n18 shape:diamond
    style n20 shape:diamond
    style n37 shape:diamond
    
    style n1, n14, n15, n25, n36 rx:100,ry:100
```

### 6. Código fuente

Se adjunta el código principal del laboratorio:
- **move_turtle2.py**: Nodo para controlar el movimiento de la tortuga y manejar las funciones de dibujo.
- **Funciones de dibujo**: Dibujar letras como `draw_S_continuous()`, `draw_A_continuous()`, etc.
- **Funciones de movimiento**: `move_timed()`, `go_to_point()`, y `rotate_to_angle()`.

### 7. Video Explicativo

A continuación, se presenta un video donde se explica el proceso de ejecución y la demostración del funcionamiento del laboratorio:

[![Ver video en YouTube](https://img.shields.io/badge/Ver%20en%20YouTube-%F0%9F%94%B4-red?style=for-the-badge)](https://youtu.be/ppMkalenVMg)

## Conclusiones
- Se logró controlar completamente la tortuga utilizando ROS 2, sin usar `turtle_teleop_key`.
- Se implementó un sistema de dibujo de letras continuas, respetando los tamaños y espaciados consistentes.
- El uso de ROS 2 y los servicios como `/reset` permitió realizar una simulación precisa de las letras.

---

**Repositorio GitHub**: [Acceder al repositorio](https://github.com/sergiosinlimites/lab4-robotics-ros2-turtlesim)
