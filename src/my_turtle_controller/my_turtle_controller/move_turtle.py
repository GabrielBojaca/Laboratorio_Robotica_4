#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import sys
import termios
import tty
import time


RATE_HZ = 50.0 

# -----------------------------
# FUNCIONES PARA LEER TECLAS
# -----------------------------
def get_key():  
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch1 = sys.stdin.read(1)

        # flechas
        if ch1 == '\x1b':     # ESC
            ch2 = sys.stdin.read(1)
            ch3 = sys.stdin.read(1)
            if ch2 == '[':
                if ch3 == 'A':
                    return 'UP'
                elif ch3 == 'B':
                    return 'DOWN'
                elif ch3 == 'C':
                    return 'RIGHT'
                elif ch3 == 'D':
                    return 'LEFT'
        return ch1.upper()    # devuelve la letra presionada
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)



# ==========================================
#              NODO PRINCIPAL
# ==========================================
class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        print("\n=== CONTROL DE LA TORTUGA (ROS2) ===")
        print("Flechas: mover manualmente")
        print("Letras: J N G A C P M E B")
        print("Q: salir")
        print("====================================\n")

        self.run()



    # --------------------------------------
    #   MOVIMIENTOS BÁSICOS
    # --------------------------------------

    def stop(self):
        msg = Twist()
        self.publisher_.publish(msg)

    def forward(self):
        msg = Twist()
        msg.linear.x = 2.0
        self.publisher_.publish(msg)

    def backward(self):
        msg = Twist()
        msg.linear.x = -2.0
        self.publisher_.publish(msg)

    def turn_left(self):
        msg = Twist()
        msg.angular.z = 10.0
        self.publisher_.publish(msg)

    def turn_right(self):
        msg = Twist()
        msg.angular.z = -10.0
        self.publisher_.publish(msg)



    # --------------------------------------
    #  MOVIMIENTO CON TIEMPO PARA DIBUJAR
    # --------------------------------------

    def forward_for(self, t):
        msg = Twist()
        msg.linear.x = 1.0

        rate = 1.0 / RATE_HZ    # 60 Hz
        steps = int(t / rate)

        for _ in range(steps):
            self.publisher_.publish(msg)
            time.sleep(rate)

        self.stop()


    def backward_for(self, t):
        msg = Twist()
        msg.linear.x = -1.0

        rate = 1.0 / RATE_HZ
        steps = int(t / rate)

        for _ in range(steps):
            self.publisher_.publish(msg)
            time.sleep(rate)

        self.stop()


    def turn_left_for(self, t):
        msg = Twist()
        msg.angular.z = 1.0    # RECOMENDADO

        rate = 1.0 / RATE_HZ
        steps = int(t / rate)

        for _ in range(steps):
            self.publisher_.publish(msg)
            time.sleep(rate)

        self.stop()


    def turn_right_for(self, t):
        msg = Twist()
        msg.angular.z = -1.0   # RECOMENDADO

        rate = 1.0 / RATE_HZ
        steps = int(t / rate)

        for _ in range(steps):
            self.publisher_.publish(msg)
            time.sleep(rate)

        self.stop()

   


    # =====================================
    #           DIBUJO DE LETRAS
    # =====================================

    # --- J ---
    def draw_J(self):

        self.forward_for(0.2) # Aproximación 
        self.forward_for(0.25) # Priemera linea 
        self.turn_left_for(3.141592/4.0) # Girar 45° 
        self.forward_for(0.25) # Segunda linea 
        self.turn_left_for(3.141592/4.0) # Girar 45° 
        self.forward_for(1.8233) # Segunda linea 
        self.turn_left_for(3.141592/2.0) # Girar 90° 
        self.forward_for(0.5) #   
        self.backward_for(1.0) #   
        self.forward_for(0.5) #   
        self.turn_left_for(3.141592/2.0) # Girar 90° 
        self.forward_for(1.8233) # Segunda linea 
        self.turn_right_for(3.141592/4.0) # Girar 45° 
        self.forward_for(0.25)
        self.turn_right_for(3.141592/4.0) # Girar 45° 
        self.forward_for(0.25)
        self.turn_left_for(3.141592) # Girar 180° 
        self.forward_for(1.2)

    # --- N ---
    def draw_N(self):
        self.forward_for(0.2) # Aproximación 
        self.turn_left_for(3.141592/2.0) # Girar 90° 
        self.forward_for(2) # Aproximación 
        self.turn_right_for(153.43*( 3.141592/180.0)) # Girar 90° 
        self.forward_for(2.236)
        self.turn_left_for(153.43*(3.141592/180.0)) # Girar 90° 
        self.forward_for(2)

        self.turn_right_for( 3.141592) # Girar 90° 
        self.forward_for(2)
        self.turn_left_for(3.141592/2.0) # Girar 90° 
        self.forward_for(0.2)


        #self.turn_right_for(157.43 * (3.141592/180.0))
        #self.forward_for(2)
        #self.turn_left_for(0.5)
        #self.forward_for(2)

    # --- G ---
    def draw_G(self):
        self.forward_for(0.2)
        self.turn_left_for(90*(3.141592/180.0))
        self.forward_for(1.8)
        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.28284)
        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.8)
        self.turn_left_for(180*(3.141592/180.0))
        self.forward_for(0.8)
        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.28284)
        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(1.8)
        self.turn_left_for(90*(3.141592/180.0))
        self.forward_for(0.8)
        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.28284)
        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.6)
        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.28284)
        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.6)
        self.turn_left_for(180*(3.141592/180.0))
        self.forward_for(0.6)
        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.28284)
        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.6)
        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.28284)
        self.turn_left_for(45*(3.141592/180.0))
        self.turn_left_for(90*(3.141592/180.0))
        self.forward_for(0.4)


    # --- A ---
    def draw_A(self):
        self.forward_for(0.2)
        self.turn_left_for(75.96*(3.141592/180.0))
        self.forward_for(2.0615)
        self.turn_right_for(75.96*2*(3.141592/180.0))
        self.forward_for(1.0607)
        self.turn_right_for((180-75.96)*(3.141592/180.0))
        self.forward_for(0.5)
        self.turn_left_for(180*(3.141592/180.0))
        self.forward_for(0.5)
        self.turn_right_for(75.96*(3.141592/180.0))
        self.forward_for(1.0607)
        self.turn_left_for(75.96*(3.141592/180.0))
        self.forward_for(0.2)


    # --- C ---
    def draw_C(self):
        self.forward_for(0.2)
        self.forward_for(0.2)

        self.turn_left_for(135*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(1.6)

        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.6)

        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_left_for(180*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.6)

        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(1.6)

        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.6)

        self.turn_left_for(45*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_left_for(180*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_left_for(135*(3.141592/180.0))
        self.forward_for(0.2)
        self.forward_for(0.2)


    # --- P ---
    def draw_P(self):
        self.forward_for(0.2)

        self.turn_left_for(90*(3.141592/180.0))
        self.forward_for(2)

        self.turn_right_for(90*(3.141592/180.0))
        self.forward_for(0.8)

        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.6)

        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.28284)

        self.turn_right_for(45*(3.141592/180.0))
        self.forward_for(0.8)

        self.turn_left_for(90*(3.141592/180.0))
        self.forward_for(1)

        self.turn_left_for(90*(3.141592/180.0))
        self.forward_for(1)

        self.forward_for(0.2)


    # --- M ---
    def draw_M(self):
        self.forward_for(2)
        self.turn_right_for(1)
        self.forward_for(1.5)
        self.turn_left_for(1)
        self.forward_for(1.5)
        self.turn_right_for(1)
        self.forward_for(2)

    # --- E ---
    def draw_E(self):
        self.forward_for(2)
        self.turn_right_for(1)
        self.forward_for(1)
        self.backward_for(1)
        self.turn_left_for(1)
        self.forward_for(1)
        self.turn_right_for(1)
        self.forward_for(1)
        self.backward_for(1)
        self.turn_left_for(1)
        self.forward_for(1)
        self.turn_right_for(1)
        self.forward_for(1)

    # --- B ---
    def draw_B(self):
        self.forward_for(2)
        self.turn_right_for(1)
        self.forward_for(1)
        self.turn_right_for(1)
        self.forward_for(1)
        self.backward_for(1)
        self.turn_left_for(1)
        self.forward_for(1)
        self.turn_left_for(1)
        self.forward_for(1)



    # =====================================
    #       LOOP PRINCIPAL (TECLADO)
    # =====================================
    def run(self):

        while rclpy.ok():

            key = get_key()

            # ---- salir ----
            if key == 'Q':
                print("Saliendo...")
                break

            # ---- flechas ----
            if key == 'UP':
                self.forward()
            elif key == 'DOWN':
                self.backward()
            elif key == 'LEFT':
                self.turn_left()
            elif key == 'RIGHT':
                self.turn_right()

            # ---- letras ----
            elif key == 'J':
                self.draw_J()
            elif key == 'N':
                self.draw_N()
            elif key == 'G':
                self.draw_G()
            elif key == 'A':
                self.draw_A()
            elif key == 'C':
                self.draw_C()
            elif key == 'P':
                self.draw_P()
            elif key == 'M':
                self.draw_M()
            elif key == 'E':
                self.draw_E()
            elif key == 'B':
                self.draw_B()

            self.stop()   # detiene entre movimientos




# ======================================
#               MAIN
# ======================================
def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()
