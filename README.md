<p align="center">
  <img src="https://github.com/user-attachments/assets/dbd3fe7d-6ee8-4415-9bd6-35dfebacb376">
</p>
<!-- ✦✦✦ FUTURE IS AUTOMATED ✦✦✦ -->
<!-- Banner superior “neón” -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=180&width=800&color=0:04041A,50:14213D,100:0A4D68&text=Laboratorio%204%20-%20Introducci%C3%B3n%20a%20ROS%202%20y%20Turtlesim&fontColor=E0FBFC&fontAlign=50&fontAlignY=30&desc=Laboratorio%204%20-%20Introducci%C3%B3n%20a%20ROS%202%20y%20Turtlesim&descAlign=50&descAlignY=60" alt="header" />
</p>

<h1 align="center">🤖 LABORATORIO 4 – INTRODUCCIÓN A ROS 2 HUMBLE - TURTLESIM</h1>

# Laboratorio 4: Introducción a ROS 2 y Turtlesim

<img src="https://github.com/user-attachments/assets/b25c60f2-1fe4-4063-85d4-3cb31e83c775" width="500"  height="500"/>



</p>

<p align="center">
  <a href="https://youtu.be/ppMkalenVMg">
    <img src="https://img.shields.io/badge/Ver%20en%20YouTube-%F0%9F%94%B4-red?style=for-the-badge" 
         alt="Ver en YouTube">
  </a>
</p>


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
graph TD;
    A[Inicio nodo TurtleController] --> B[Suscribirse a /turtle1/pose];
    B --> C[Crear publisher /turtle1/cmd_vel];
    C --> D[Crear cliente /reset];
    D --> E[Esperar tecla en bucle];
    E --> F[Control manual send_cmd(linear, angular)];
    E --> G[Secuencias SABP y SFRM];
    F --> H[Limpiar trazo (reset_simulation)];
    G --> I[Ir al origen (move_to_start_L)];
    H --> J[Salir];
    click A "https://github.com/user-lab4" "Go to GitHub Repo"
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
