import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/elreyrtubuntu/lab-robotica/lab-4-robotica/install/my_turtle_controller'
