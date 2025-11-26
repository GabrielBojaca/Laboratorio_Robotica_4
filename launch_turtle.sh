#!/bin/bash

# ================================
#  Script para lanzar Turtlesim
#  y controlador en 2 terminales
# ================================


# Ejecuta turtlesim en nueva terminal
gnome-terminal -- bash -c "
	source /opt/ros/humble/setup.bash 
    	echo '=== Lanzando turtlesim_node ===';
    	ros2 run turtlesim turtlesim_node;
    	exec bash
"

# Espera 1 segundo
sleep 1

# Ejecuta el controlador 
gnome-terminal -- bash -c "
	source /opt/ros/humble/setup.bash 
	echo '=== Lanzando controlador de tortuga ===';
    	ros2 run my_turtle_controller move_turtle;
    	exec bash
"

